# Calculator Developed by Kirklen Allen
import math

# Addition
def add(num1, num2):
    return num1 + num2

# Subtraction
def subtract(num1, num2):
    return num1 - num2

# Multiply
def multiply(num1, num2):
    return num1 * num2

# Divide
def divide(num1, num2):
    if num2 == 0:  # Fix this to check if `num2` is zero, not `num1` (update)
        return "Division by zero is undefined."
    return num1 / num2

# Square Root
def square(num):
    if num >= 0:
        return math.sqrt(num)
    else:
        return "Square root of a negative number is undefined."

# The calculator combines all of the functions to create a cohesive math program
def calculator():
    print("Booting Basic Calculator v1.0 Developed by Kirklen Allen")
    print("Select an Operation")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Square Root")
    print("6. Exit")

    while True:
        try:
            select = int(input("Select the number of the Operation you would like to calculate: "))
            if select == 6:
                print("Thank you for using Basic Calculator v1.0 Developed by Kirklen Allen. Farewell! :D")
                break

            if select not in range(1, 6):
                print("Invalid Input. Please select a number from 1 to 6.")
                continue

            if select == 5:
                # Square root operation requires only one number
                number = float(input("Enter the number to calculate the square root: "))
                print(f"The square root of {number} is {square(number)}")
            else:
                # Other operations require two numbers
                number1 = float(input("Enter first number: "))
                number2 = float(input("Enter second number: "))

                if select == 1:
                    print(f"The result is: {add(number1, number2)}")
                elif select == 2:
                    print(f"The result is: {subtract(number1, number2)}")
                elif select == 3:
                    print(f"The result is: {multiply(number1, number2)}")
                elif select == 4:
                    print(f"The result is: {divide(number1, number2)}")

        except ValueError:
            print("Invalid Input. Please use numbers.")

# Run the program
if __name__ == "__main__":
    calculator()
