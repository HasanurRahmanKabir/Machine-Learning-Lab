# Create a simple calculator that performs basic arithmetic operations (addition, subtraction, multiplication, division) based on user input.

x = float(input("Enter the first number: "))
y = float(input("Enter the second number: "))

operation = input("Enter the operation (+, -, *, /): ")

if operation == "+":
    result = x + y
elif operation == "-":
    result = x - y
elif operation == "*":
    result = x * y
elif operation == "/":
    result = x / y
else:
    print("Invalid operation")
    result = None

if result is not None:
    print(f"{x} {operation} {y}: {result}")