
def get_user_query(username):
    # INTENTIONALLY VULNERABLE DEMO:
    # User input is concatenated into SQL.
    query = "SELECT * FROM users WHERE username = '" + username + "'"
    return query
