num1 = input("Enter the first value: ")
num2 = input("Enter the second value: ")
operation = input("Enter operation (+, -, *, /, **, %): ")

# Check if both inputs are numbers
if num1.replace('.', '', 1).isdigit() and num2.replace('.', '', 1).isdigit():
    num1 = float(num1)
    num2 = float(num2)

    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == '/':
        if num2 == 0:
            result = "Error: Division by zero is not allowed."
        else:
            result = num1 / num2
    elif operation == '**':
        result = num1 ** num2
    elif operation == '%':
        result = num1 % num2
    else:
        result = "Invalid operation."
    
# If inputs are strings, allow string operations
else:
    if operation == '+':
        result = num1 + num2  # String concatenation
    elif operation == '*' and num2.isdigit():
        result = num1 * int(num2)  # String repetition
    else:
        result = "Invalid operation for strings."

print(f"Result: {result}")
