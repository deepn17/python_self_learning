
def add(a, b):
    """Add two values using the '+' operator"""
    return a + b

def subtract(a, b):
    """Subtract two values using the '-' operator"""
    return a - b

def multiply(a, b):
    """Multiply two values using the '*' operator"""
    return a * b

def divide(a, b):
    """Divide two values using the '/' operator"""
    if b == 0:
        return "Cannot divide by Zero"
    return a / b

print(add(2,3))
print(subtract(5, 2))
print(multiply(7, 3))
print(divide(7, 0))
print(divide(9, 3))