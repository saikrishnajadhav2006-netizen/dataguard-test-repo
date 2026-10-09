import sqlite3

def find_user(username, password):
    connection = sqlite3.connect("users.db")

    # INTENTIONAL SECURITY ISSUE: SQL injection
    query = "SELECT * FROM users WHERE username = '" + username + "' AND password = '" + password + "'"

    cursor = connection.cursor()
    cursor.execute(query)

    result = cursor.fetchone()
    connection.close()

    return result
