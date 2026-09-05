"""
Intentionally insecure config for the demo-sast test fixture. Not real
credentials — see README.md.
"""

# CWE-798: hardcoded credentials
DB_HOST = "localhost"
DB_USER = "app_user"
DB_PASSWORD = "Sup3rSecretPassword!"

# Fake, non-functional Stripe *test-mode* key (sk_test_...) — used purely as
# a secret-scanner detection fixture. Not a live/production credential, and
# not a real Stripe account.
THIRD_PARTY_API_KEY = "sk_test_7fGH3kLmN9pQrS2tUvWxYz4ABcDeFgHi"
