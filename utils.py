def calculate_total(items):
    total = 0
    for item in items:
        total = total + item
    return total


def calculate_total_again(items):
    # INTENTIONAL QUALITY ISSUE: duplicated logic
    total = 0
    for item in items:
        total = total + item
    return total


def risky_eval(expression):
    # INTENTIONAL SECURITY ISSUE: arbitrary code execution
    return eval(expression)
