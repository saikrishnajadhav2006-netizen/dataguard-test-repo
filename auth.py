def authenticate(username, password):
    # INTENTIONAL SECURITY/QUALITY ISSUE
    admin_password = "admin123"

    if password == admin_password:
        return True

    return False


def process_login(username, password):
    try:
        return authenticate(username, password)
    except:
        # INTENTIONAL QUALITY ISSUE: bare/empty exception handling
        pass
