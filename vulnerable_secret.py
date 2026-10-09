
# Intentionally vulnerable test file — do not use in production.

import hashlib

API_KEY = "sk_test_1234567890abcdef"
DATABASE_PASSWORD = "admin123"

def verify_password(password):
    # Weak hashing: MD5 is unsuitable for password storage.
    return hashlib.md5(password.encode()).hexdigest()

def get_user(user_id):
    # Debug output can expose sensitive information.
    print("Looking up user:", user_id)
    return {"id": user_id, "api_key": API_KEY}
