import Head from "next/head";
import { useEffect, useRef, useState } from "react";

const sessionPath = "/api/v1/session";

export default function LocalSession() {
  const [active, setActive] = useState(false);
  const [message, setMessage] = useState("");
  const [busy, setBusy] = useState(true);
  const input = useRef(null);

  useEffect(() => {
    let mounted = true;
    fetch(sessionPath, { cache: "no-store" })
      .then((response) => {
        if (mounted && response.ok) {
          setActive(true);
          setMessage("Session active.");
        }
      })
      .catch(() => mounted && setMessage("Local service unavailable."))
      .finally(() => mounted && setBusy(false));
    return () => { mounted = false; };
  }, []);

  async function submit(event) {
    event.preventDefault();
    if (busy) return;
    setBusy(true);
    const headers = active ? {} : { "X-SpecGuard-Bootstrap": input.current.value };
    if (input.current) input.current.value = "";
    try {
      const response = await fetch(sessionPath, { method: active ? "DELETE" : "POST", headers });
      if (response.ok) {
        setActive(!active);
        setMessage(active ? "Session ended." : "Session active.");
      } else {
        setActive(false);
        setMessage("Session request denied.");
      }
    } catch {
      setMessage("Local service unavailable.");
    } finally {
      setBusy(false);
    }
  }

  return (
    <main>
      <Head><title>Local session · SpecGuard</title></Head>
      <header>SpecGuard</header>
      <section>
        <h1>Local session</h1>
        <p>This controlled check grants access to session status only.</p>
        <form method="post" onSubmit={submit}>
          {!active && <label>Terminal code
            <input type="password" ref={input} autoComplete="off" spellCheck={false} required />
          </label>}
          <button disabled={busy}>{active ? "End session" : "Start session"}</button>
        </form>
        <p role="status">{message}</p>
      </section>
    </main>
  );
}
