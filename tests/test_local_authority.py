"""SG-R031-AC01 component oracles from the verification policy and owner decision."""

import asyncio
import unittest
from contextlib import AsyncExitStack

import httpx

from specguard.app import create_app
from specguard.local import LocalAddress


class AuthorityTests(unittest.IsolatedAsyncioTestCase):
    async def asyncSetUp(self):
        self.now = 0
        self.codes = []
        self.origin = "http://127.0.0.1:49152"
        self.address = LocalAddress(49152)
        self.stack = AsyncExitStack()
        self.addAsyncCleanup(self.stack.aclose)
        await self.start()

    async def start(self):
        self.app = create_app(self.address, self.codes.append, clock=lambda: self.now)
        await self.stack.enter_async_context(self.app.router.lifespan_context(self.app))
        self.client = await self.stack.enter_async_context(
            httpx.AsyncClient(
                base_url=self.origin,
                transport=httpx.ASGITransport(app=self.app),
                trust_env=False,
            )
        )

    async def bootstrap(self, code=None, origin=None):
        return await self.client.post(
            "/api/v1/session",
            headers={
                "Origin": origin or self.origin,
                "X-SpecGuard-Bootstrap": self.codes[-1] if code is None else code,
            },
        )

    async def test_single_use_bootstrap_and_cookie(self):
        self.assertEqual(len(self.codes[0]), 43)
        self.assertEqual((await self.bootstrap("synthetic-invalid")).status_code, 403)
        first, second = await asyncio.gather(self.bootstrap(), self.bootstrap())
        self.assertEqual(sorted([first.status_code, second.status_code]), [204, 403])
        reply = first if first.status_code == 204 else second
        cookie = reply.headers["set-cookie"]
        for attr in ("httponly", "samesite=strict", "path=/"):
            self.assertIn(attr, cookie.lower().split("; "))
        self.assertNotIn("domain=", cookie.lower())
        self.assertFalse(self.codes[0] in cookie)
        self.assertEqual(reply.content, b"")
        self.assertEqual((await self.client.get("/api/v1/session")).status_code, 200)

    async def test_denials_precede_bootstrap_and_revoke(self):
        headers = {"X-SpecGuard-Bootstrap": self.codes[0]}
        for forged in (
            {},
            {"Origin": "null"},
            {"Origin": "https://127.0.0.1:49152"},
            {"Origin": "http://localhost:49152"},
            {"Origin": self.origin + "/"},
            {"Origin": self.origin, "Host": "127.0.0.1"},
            {"Origin": self.origin, "Host": "localhost:49152"},
            {"Origin": self.origin, "Host": "127.0.0.1:49153"},
            {
                "Forwarded": "host=127.0.0.1:49152",
                "X-Forwarded-Host": "127.0.0.1:49152",
            },
        ):
            with self.subTest(headers=list(forged)):
                reply = await self.client.post(
                    "/api/v1/session", headers=headers | forged
                )
                self.assertEqual(reply.status_code, 403)
                self.assertNotIn("set-cookie", reply.headers)
        self.assertEqual((await self.bootstrap()).status_code, 204)
        for bad in ({}, {"Origin": "http://untrusted.invalid"}):
            self.assertEqual(
                (await self.client.delete("/api/v1/session", headers=bad)).status_code,
                403,
            )
        self.assertEqual((await self.client.get("/api/v1/session")).status_code, 200)
        self.assertEqual(
            (
                await self.client.get("/api/v1/session", headers={"Origin": "null"})
            ).status_code,
            403,
        )
        cookie = self.client.cookies.get("sg_session_49152")
        self.assertTrue(cookie)
        self.assertEqual(
            (
                await self.client.delete(
                    "/api/v1/session", headers={"Origin": self.origin}
                )
            ).status_code,
            204,
        )
        replay = await self.client.get(
            "/api/v1/session", headers={"Cookie": "sg_session_49152=" + cookie}
        )
        self.assertEqual(replay.status_code, 403)
        self.assertFalse(cookie in replay.text)

    async def test_expiry_boundaries(self):
        self.assertEqual((await self.bootstrap()).status_code, 204)
        self.now = 1799
        self.assertEqual((await self.client.get("/api/v1/session")).status_code, 200)
        self.now += 1800
        self.assertEqual((await self.client.get("/api/v1/session")).status_code, 403)
        await self.start()
        self.assertEqual((await self.bootstrap()).status_code, 204)
        issued = self.now
        for elapsed in range(1200, 28800, 1200):
            self.now = issued + elapsed
            self.assertEqual(
                (await self.client.get("/api/v1/session")).status_code, 200
            )
        self.now = issued + 28800
        self.assertEqual((await self.client.get("/api/v1/session")).status_code, 403)

    async def test_restart_invalidates_issued_and_unused_proofs(self):
        old_code = self.codes[0]
        await self.stack.aclose()
        await self.start()
        self.assertEqual((await self.bootstrap(old_code)).status_code, 403)
        self.assertEqual((await self.bootstrap()).status_code, 204)
        cookies = dict(self.client.cookies)
        await self.stack.aclose()
        await self.start()
        self.client.cookies.update(cookies)
        self.assertEqual((await self.client.get("/api/v1/session")).status_code, 403)

    async def test_missing_invalid_and_duplicate_authority(self):
        for headers in (
            [],
            [("Cookie", "sg_session_49152=synthetic-invalid")],
            [("Host", "127.0.0.1:49152"), ("Host", "127.0.0.1:49152")],
        ):
            reply = await self.client.get("/api/v1/session", headers=headers)
            self.assertEqual(reply.status_code, 403)
        code_header = ("X-SpecGuard-Bootstrap", self.codes[0])
        origin = ("Origin", self.origin)
        for headers in (
            [origin, origin, code_header],
            [origin, code_header, code_header],
        ):
            self.assertEqual(
                (
                    await self.client.post("/api/v1/session", headers=headers)
                ).status_code,
                403,
            )
        await self.bootstrap()
        cookie = "sg_session_49152=" + self.client.cookies["sg_session_49152"]
        for headers in (
            [("Cookie", cookie), ("Cookie", cookie)],
            [("Cookie", cookie + "; " + cookie)],
        ):
            self.assertEqual(
                (await self.client.get("/api/v1/session", headers=headers)).status_code,
                403,
            )

    async def test_unauthorized_body_never_consumed_and_errors_are_safe(self):
        # Direct ASGI ingress lets receive() be an independently observed tripwire.
        sent = []

        async def send(message):
            sent.append(message)

        async def receive():
            self.fail("unauthorized request body consumed")

        scope = {
            "type": "http",
            "asgi": {"version": "3.0"},
            "http_version": "1.1",
            "method": "POST",
            "scheme": "http",
            "path": "/api/v1/audits",
            "root_path": "",
            "raw_path": b"/api/v1/audits",
            "query_string": b"synthetic-marker",
            "server": ("127.0.0.1", 49152),
            "client": ("127.0.0.1", 12345),
            "headers": [(b"host", b"127.0.0.1:49152")],
        }
        await self.app(scope, receive, send)
        self.assertEqual(sent[0]["status"], 403)
        self.assertNotIn(b"synthetic-marker", sent[-1]["body"])
        self.assertEqual(dict(sent[0]["headers"])[b"cache-control"], b"no-store")

    async def test_no_product_routes_after_session_establishment(self):
        await self.bootstrap()
        for path in ("/api/v1/audits", "/docs", "/openapi.json"):
            reply = await self.client.get(path)
            self.assertEqual(reply.status_code, 403)
            self.assertNotIn("set-cookie", reply.headers)


class ConfigTests(unittest.TestCase):
    def test_explicit_port_and_ipv4_loopback(self):
        for port in (0, -1, 65536, True, "8000"):
            with self.subTest(port=port), self.assertRaises(ValueError):
                LocalAddress(port)
        for port in (1, 65535):
            self.assertEqual(LocalAddress(port).origin, f"http://127.0.0.1:{port}")
