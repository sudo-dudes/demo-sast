# demo-sast

A deliberately vulnerable Flask app used to test Perimetr's SAST-scanning
prototype (Opengrep + Gitleaks). Every issue in `app.py` and `config.py` is
intentional — this code exists to be flagged, not to run in production.

Do not deploy this. Do not copy these patterns into real code.

## What's seeded here, and why

| File | Pattern | Roughly maps to |
|---|---|---|
| `app.py` | `os.system` built from a request param | CWE-78 (OS command injection) |
| `app.py` | SQL query built with an f-string | CWE-89 (SQL injection) |
| `app.py` | `pickle.loads` on request body | CWE-502 (insecure deserialization) |
| `app.py` | path built from a request param, no sanitization | CWE-22 (path traversal) |
| `app.py` | `hashlib.md5` for password hashing | CWE-327 (broken/weak crypto) |
| `config.py` | hardcoded DB password | CWE-798 (hardcoded credentials) |
| `config.py` | fake `sk_test_...` key (Stripe test-mode format, not a real account) | secret-detection test fixture (Gitleaks) |

Note: an earlier version of this fixture used AWS's own published example
access key (`AKIAIOSFODNN7EXAMPLE`). Gitleaks' default config explicitly
allowlists anything ending in `EXAMPLE`, so it never actually got flagged —
swapped for a fake Stripe-test-key-shaped string instead, which does.
