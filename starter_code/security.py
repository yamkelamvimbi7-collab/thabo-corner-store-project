
"""
security.py
------------
Task 6: Basic access control and password hashing.
"""

import hashlib
import getpass
import hmac


def hash_password(plain_text_password: str) -> str:
    """Convert a password into a SHA-256 hash."""
    return hashlib.sha256(
        plain_text_password.encode("utf-8")
    ).hexdigest()


def check_password(attempt: str, stored_hash: str) -> bool:
    """Check a password against its stored hash."""
    attempted_hash = hash_password(attempt)
    return hmac.compare_digest(attempted_hash, stored_hash)


def login_gate(stored_hash: str, max_attempts: int = 3) -> bool:
    """Allow access after a correct password, with limited attempts."""
    for attempt_number in range(max_attempts):
        attempt = getpass.getpass(
            "Enter password to view reports: "
        )

        if check_password(attempt, stored_hash):
            print("Access granted.")
            return True
        else:
            print("Incorrect password. Try again.")

    print("Access denied - too many failed attempts.")
    return False


# Learning example: replace this with a hash of your chosen password.
# Do not store the actual password in this file.
STORED_PASSWORD_HASH = hash_password("StoreDemo2026!")
