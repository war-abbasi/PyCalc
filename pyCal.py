import math

# Function to add two numbers
def add(x, y):
    return x + y

# Function to subtract two numbers
def subtract(x, y):
    return x - y

# Function to multiply two numbers
def multiply(x, y):
    return x * y

# Function to divide two numbers
def divide(x, y):
    if y == 0:
        return "Error: Division by zero!"
    return x / y

# Function to calculate square root
def square_root(x):
    if x < 0:
        return "Error: Imaginary result!"
    return math.sqrt(x)

# Function to calculate power
def power(x, y):
    return x ** y

# Function to calculate sine
def sin(x):
    return math.sin(x)

# Function to calculate cosine
def cos(x):
    return math.cos(x)

# Function to calculate tangent
def tan(x):
    return math.tan(x)

print("Simple Arithmetic and Scientific Calculator")

while True:
    print("\nOperations:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Square Root")
    print("6. Power")
    print("7. Sine")
    print("8. Cosine")
    print("9. Tangent")
    print("10. Quit")

    choice = input("Enter choice: ")

    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print("Result:", add(num1, num2))
        elif choice == '2':
            print("Result:", subtract(num1, num2))
        elif choice == '3':
            print("Result:", multiply(num1, num2))
        elif choice == '4':
            print("Result:", divide(num1, num2))
    elif choice == '5':
        num = float(input("Enter a number: "))
        print("Result:", square_root(num))
    elif choice == '6':
        num1 = float(input("Enter base number: "))
        num2 = float(input("Enter exponent: "))
        print("Result:", power(num1, num2))
    elif choice == '7':
        angle = float(input("Enter angle in radians: "))
        print("Result:", sin(angle))
    elif choice == '8':
        angle = float(input("Enter angle in radians: "))
        print("Result:", cos(angle))
    elif choice == '9':
        angle = float(input("Enter angle in radians: "))
        print("Result:", tan(angle))
    elif choice == '10':
        print("Exiting calculator. Goodbye!")
        break
    else:
        print("Invalid input. Please enter a valid choice.")
