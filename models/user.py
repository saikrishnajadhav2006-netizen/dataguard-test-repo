class User:
    def __init__(self, username, password):
        self.username = username
        # INTENTIONAL QUALITY/SECURITY ISSUE:
        # Plain-text password stored on the model.
        self.password = password
