from flask import request
import sqlite3

def get_user_controller():
    # INTENTIONAL ARCHITECTURE ISSUE:
    # Controller directly performs database access and business logic.
    username = request.args.get("username")

    connection = sqlite3.connect("users.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
    user = cursor.fetchone()
    connection.close()

    if user:
        return {"status": "success", "user": user}

    return {"status": "not_found"}
