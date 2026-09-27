# Simple Python Calculator - Project 1 by Gomolemo
print("=== My Python Calculator ===")

def calculator():
    try:
        num1 = float(input("Enter first number: "))
        operator = input("Enter operator (+, -, *, /): ")
        num2 = float(input("Enter second number: "))

        if operator == "+":
            result = num1 + num2
        elif operator == "-":
            result = num1 - num2
        elif operator == "*":
            result = num1 * num2
        elif operator == "/":
            if num2 == 0:
                return "Error: Cannot divide by zero"
            result = num1 / num2
        else:
            return "Invalid operator"

        return f"Result: {num1} {operator} {num2} = {result}"
    except ValueError:
        return "Error: Please enter valid numbers"

# Run it
print(calculator())