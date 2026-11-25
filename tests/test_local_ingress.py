"""Controlled real HTTP and browser observations of the local foundation."""

import io
import multiprocessing
import os
import socket
import subprocess
import sys
import threading
import time
import unittest
from contextlib import contextmanager, redirect_stderr, redirect_stdout
from unittest.mock import Mock

import httpx

from specguard.server import bind_listener, make_server


@contextmanager
def running_server(clock=time.monotonic):
    codes = []
    with bind_listener(0) as listener:
        host, port = listener.getsockname()
        assert host == "127.0.0.1"
        server = make_server(listener, codes.append, clock=clock)
        thread = threading.Thread(
            target=server.run, kwargs={"sockets": [listener]}, daemon=True
        )
        thread.start()
        try:
            deadline = time.monotonic() + 10
            while not server.started:
                if not thread.is_alive() or time.monotonic() >= deadline:
                    raise RuntimeError("Local fixture failed to start")
                time.sleep(0.01)
            yield f"http://{host}:{port}", codes[0]
        finally:
            server.should_exit = True
            thread.join(10)
            if thread.is_alive():
                raise RuntimeError("Local fixture failed to stop")


def child_listener(channel):
    with channel, running_server() as (origin, code):
        channel.send((origin, code))
        channel.recv()


@contextmanager
def fresh_process():
    ctx = multiprocessing.get_context("spawn")
    parent, child = ctx.Pipe()
    process = ctx.Process(target=child_listener, args=(child,))
    process.start()
    child.close()
    try:
        if not parent.poll(20):
            raise RuntimeError("Child listener unavailable")
        yield parent.recv()
        parent.send("stop")
        process.join(10)
        if process.exitcode != 0:
            raise RuntimeError("Child listener failed to stop cleanly")
    finally:
        parent.close()
        if process.is_alive():
            process.terminate()
            process.join(5)


class IngressTests(unittest.TestCase):
    def test_noninteractive_cli_refuses_bootstrap(self):
        run = subprocess.run(
            [sys.executable, "-m", "specguard", "--local-check"],
            check=False,
            stdin=subprocess.DEVNULL,
            capture_output=True,
            timeout=10,
        )
        self.assertEqual(run.returncode, 2)
        self.assertEqual(run.stdout, b"")
        self.assertIn(b"interactive local terminal", run.stderr)

    def test_prior_process_proofs_denied_on_fresh_listener(self):
        route = "/api/v1/session"
        with fresh_process() as (_, unused_code):
            pass
        with (
            fresh_process() as (second, code),
            httpx.Client(base_url=second, trust_env=False) as client,
        ):

            def exchange(value):
                return client.post(
                    route, headers={"Origin": second, "X-SpecGuard-Bootstrap": value}
                )

            self.assertEqual(exchange(unused_code).status_code, 403)
            self.assertEqual(exchange(code).status_code, 204)
            (old_token,) = client.cookies.values()
        with (
            fresh_process() as (third, _),
            httpx.Client(base_url=third, trust_env=False) as client,
        ):
            name = f"sg_session_{httpx.URL(third).port}"
            self.assertEqual(
                client.get(
                    route, headers={"Cookie": name + "=" + old_token}
                ).status_code,
                403,
            )

    def test_expiry_and_invalid_requests_at_http_ingress(self):
        route = "/api/v1/session"
        for boundary in ("idle", "absolute"):
            clock = Mock(return_value=0)
            with (
                self.subTest(boundary=boundary),
                running_server(clock) as (origin, code),
                httpx.Client(base_url=origin, trust_env=False) as client,
            ):
                headers = {"Origin": origin, "X-SpecGuard-Bootstrap": code}
                for path, body in [
                    (route + "?synthetic-marker", b""),
                    (route, b"synthetic-marker"),
                ]:
                    response = client.post(path, headers=headers, content=body)
                    self.assertEqual(response.status_code, 403)
                    self.assertNotIn("synthetic-marker", response.text)
                    self.assertNotIn("set-cookie", response.headers)
                self.assertEqual(client.post(route, headers=headers).status_code, 204)
                if boundary == "absolute":
                    for now in range(1200, 28800, 1200):
                        clock.return_value = now
                        self.assertEqual(client.get(route).status_code, 200)
                    clock.return_value = 28800
                else:
                    clock.return_value = 1799
                    self.assertEqual(
                        client.get(
                            route, headers={"Cookie": "invalid=synthetic-marker"}
                        ).status_code,
                        403,
                    )
                    clock.return_value = 1800
                self.assertEqual(client.get(route).status_code, 403)

    def test_request_markers_stay_out_of_http_errors_and_diagnostics(self):
        output = io.StringIO()
        marker = "synthetic-request-marker"
        with (
            redirect_stdout(output),
            redirect_stderr(output),
            running_server() as (origin, code),
        ):
            with httpx.Client(base_url=origin, trust_env=False) as client:
                reply = client.post(
                    "/api/v1/audits?" + marker,
                    content=marker,
                    headers={"Cookie": "fixture=" + marker},
                )
                self.assertEqual(reply.status_code, 403)
                self.assertFalse(marker in reply.text)
            endpoint = httpx.URL(origin)
            with socket.create_connection(
                (endpoint.host, endpoint.port), timeout=3
            ) as peer:
                peer.sendall(b"INVALID REQUEST synthetic-request-marker\r\n\r\n")
                reply = peer.recv(4096)
                self.assertTrue(reply.startswith(b"HTTP/1.1 400"))
                self.assertNotIn(marker.encode(), reply)
        self.assertFalse(marker in output.getvalue())
        self.assertFalse(code in output.getvalue())

    def test_real_listener_session_and_shutdown(self):
        with (
            running_server() as (origin, code),
            httpx.Client(base_url=origin, trust_env=False) as client,
        ):
            route = "/api/v1/session"
            self.assertEqual(client.get(route).status_code, 403)
            self.assertEqual(
                client.post(route, headers={"X-SpecGuard-Bootstrap": code}).status_code,
                403,
            )
            self.assertEqual(
                client.post(
                    route,
                    headers={
                        "Origin": "http://localhost",
                        "X-SpecGuard-Bootstrap": code,
                    },
                ).status_code,
                403,
            )
            self.assertEqual(
                client.get("/", headers={"Host": "localhost"}).status_code, 403
            )
            bootstrap = client.post(
                route, headers={"Origin": origin, "X-SpecGuard-Bootstrap": code}
            )
            self.assertEqual(bootstrap.status_code, 204)
            self.assertEqual(client.get(route).json(), {"session": "active"})
            self.assertEqual(client.delete(route).status_code, 403)
            self.assertEqual(
                client.delete(route, headers={"Origin": origin}).status_code, 204
            )
            self.assertEqual(client.get(route).status_code, 403)
            parsed = httpx.URL(origin)
        with self.assertRaises(OSError):
            socket.create_connection((parsed.host, parsed.port), timeout=1)


@unittest.skipUnless(
    os.environ.get("SPECGUARD_TEST_BROWSER"),
    "set SPECGUARD_TEST_BROWSER to an approved browser executable",
)
class BrowserTests(unittest.TestCase):
    def test_browser_bootstrap_and_revoke(self):
        from playwright.sync_api import sync_playwright

        with running_server() as (origin, code), sync_playwright() as pw:
            browser = pw.chromium.launch(
                executable_path=os.environ["SPECGUARD_TEST_BROWSER"],
                args=["--disable-background-networking"],
            )
            try:
                # Reproduction target for the SG-05A browser observation.
                self.assertEqual(browser.version, "157.0.8103.79")
                context = browser.new_context(service_workers="block")
                page = context.new_page()
                external = []

                def restrict(route):
                    if route.request.url.startswith(origin + "/"):
                        route.continue_()
                    else:
                        external.append(route.request.url.split(":", 1)[0])
                        route.abort()

                context.route("**/*", restrict)
                page.goto(origin)
                page.get_by_label("Terminal code").fill(code)
                page.get_by_role("button", name="Start session").click()
                page.get_by_text("Session active.", exact=True).wait_for()
                self.assertFalse(
                    page.evaluate("document.cookie.includes('sg_session_')")
                )
                self.assertFalse(code in page.url)
                self.assertTrue(
                    page.evaluate(
                        "localStorage.length === 0 && sessionStorage.length === 0"
                    )
                )
                page.reload()
                page.get_by_role("button", name="End session").click()
                page.get_by_text("Session ended.", exact=True).wait_for()
                self.assertEqual(
                    page.request.get(origin + "/api/v1/session").status, 403
                )
                self.assertEqual(external, [])
            finally:
                browser.close()
