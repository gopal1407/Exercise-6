#Task 1

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error! Division by zero is not allowed."

# Example usage
if __name__ == "__main__":
    print("Welcome to the Calculator App!")
    
    # Input for the two numbers
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    # Input for the operation
    operation = input("Enter the operation (+, -, *, /): ")

    # Perform the chosen operation and display the result
    if operation == "+":
        print(f"The result of addition is: {add(num1, num2)}")
    elif operation == "-":
        print(f"The result of subtraction is: {subtract(num1, num2)}")
    elif operation == "*":
        print(f"The result of multiplication is: {multiply(num1, num2)}")
    elif operation == "/":
        print(f"The result of division is: {divide(num1, num2)}")
    else:
        print("Invalid operation.")


        #Task 2

def add(a, b):
    return a + b

# Function for subtraction
def subtract(a, b):
    return a - b

# Function for multiplication
def multiply(a, b):
    return a * b

# Function for division
def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error! Division by zero is not allowed."

# Main program
if __name__ == "__main__":
    print("Welcome to the Calculator App!")

    # Ask the user for the operation they want to perform
    operation = input("Enter the operation you want to perform (+ for addition, - for subtraction, * for multiplication, / for division): ")

    # Ask the user for the numbers they want to use
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        exit()

    # Perform the chosen operation and display the result
    if operation == "+":
        print(f"The result of addition is: {add(num1, num2)}")
    elif operation == "-":
        print(f"The result of subtraction is: {subtract(num1, num2)}")
    elif operation == "*":
        print(f"The result of multiplication is: {multiply(num1, num2)}")
    elif operation == "/":
        print(f"The result of division is: {divide(num1, num2)}")
    else:
        print("Invalid operation. Please enter one of +, -, *, or /.")


#Task 3

# Function for addition
def add(a, b):
    return a + b

# Function for subtraction
def subtract(a, b):
    return a - b

# Function for multiplication
def multiply(a, b):
    return a * b

# Function for division with error handling for division by zero
def divide(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        return "Error! Division by zero is not allowed."

if __name__ == "__main__":
    print("Welcome to the Calculator App!")

    operation = input("Enter the operation you want to perform (+ for addition, - for subtraction, * for multiplication, / for division): ")

    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        exit()

    if operation == "+":
        print(f"The result of addition is: {add(num1, num2)}")
    elif operation == "-":
        print(f"The result of subtraction is: {subtract(num1, num2)}")
    elif operation == "*":
        print(f"The result of multiplication is: {multiply(num1, num2)}")
    elif operation == "/":
        result = divide(num1, num2)
        if result == "Error! Division by zero is not allowed.":
            print(result)
        else:
            print(f"The result of division is: {result}")
    else:
        print("Invalid operation. Please enter one of +, -, *, or /.")