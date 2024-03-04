def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Cannot divide by zero"

# Example usage:
a = float(input("Enter first number: "))
operator = input("Enter operator (+, -, *, /): ")
b = float(input("Enter second number: "))

if operator == "+":
    result = add(a, b)
elif operator == "-":
    result = subtract(a, b)
elif operator == "*":
    result = multiply(a, b)
elif operator == "/":
    result = divide(a, b)
else:
    result = "Invalid operator"

print("Result:", result)