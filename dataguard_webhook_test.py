"""
Small sample module for testing DataGuard's push webhook.
"""

def greet(name):
    """Return a greeting for the supplied name."""
    return f"Hello, {name}!"

if __name__ == "__main__":
    print(greet("DataGuard"))
