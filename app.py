from flask import Flask, request
from database import find_user

app = Flask(__name__)

# INTENTIONAL SECURITY ISSUE: hardcoded secret
SECRET_KEY = "super-secret-password-12345"
API_KEY = "sk-test-hardcoded-key-123456"

@app.route("/login")
def login():
    username = request.args.get("username")
    password = request.args.get("password")

    # INTENTIONAL QUALITY ISSUE: debug output
    print("Login attempt:", username, password)

    # INTENTIONAL QUALITY ISSUE: weak validation
    if username and password:
        return find_user(username, password)

    return "Invalid login"

@app.route("/run")
def run_command():
    import os

    command = request.args.get("command")

    # INTENTIONAL SECURITY ISSUE: command injection
    os.system(command)

    return "Command executed"
