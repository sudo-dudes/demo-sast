"""
Intentionally insecure config for the demo-sast test fixture. Not real
credentials — see README.md.
"""

# CWE-798: hardcoded credentials
DB_HOST = "localhost"
DB_USER = "app_user"
DB_PASSWORD = "Sup3rSecretPassword!"

# AWS's own published example access key (never a live credential) — used
# here purely as a secret-scanner detection fixture.
AWS_ACCESS_KEY_ID = "AKIAIOSFODNN7EXAMPLE"
AWS_SECRET_ACCESS_KEY = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"
