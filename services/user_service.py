def get_user(username):
    # INTENTIONAL ARCHITECTURE ISSUE:
    # Service directly constructs database access instead of using a repository layer.
    import sqlite3

    connection = sqlite3.connect("users.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
    user = cursor.fetchone()
    connection.close()

    return user
