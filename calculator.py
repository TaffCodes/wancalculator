def calculator():
    # Ask the user to input two numbers
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    
    # Ask input for mathematical operation
    operation = input("Enter the operation (+, -, *, /): ")
    
    # Perform the operation and return result
    if operation == '+':
        result = num1 + num2
        print(f"{num1} + {num2} = {result}")
    elif operation == '-':
        result = num1 - num2
        print(f"{num1} - {num2} = {result}")
    elif operation == '*':
        result = num1 * num2
        print(f"{num1} * {num2} = {result}")
    elif operation == '/':
        if num2 != 0:
            result = num1 / num2
            print(f"{num1} / {num2} = {result}")
        else:
            print("Impoooosibo.")
    else:
        print("Invalid operation. Please enter one of +, -, *, /.")

# Run the calculator function
calculator()