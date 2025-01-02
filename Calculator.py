#Calculator Developed by Kirklen Allen
import math


#Allows the program to handle advance Arithmetic such as square roots and negative numbers.


#Addition
def add(num1, num2):
    return num1 + num2

#Subtraction
def subtract(num1, num2):
    return num1 - num2

#Multiply
def multiply(num1, num2):
    return num1 * num2

#Divide
def divide(num1, num2):
    if num1 == 0:
        return "Division by zero is known as undefined"
    return num1 / num2

#SquareRoot
def square(num):
    if num >= 0:
        return sqrt(num)

#The calculator combines all of the functions to create a cohesive math program
def calculator():
    print("Booting Basic Calculator v1.0 Developed by Kirklen Allen")
    print("Select a Operation")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. SquareRoot (Coming Soon)")
    print("6. Exit")

    while True:
        try:
            select = int(input("Select the number of the Operation you would like to calculate: "))
            if select == 6:
                print("Thank You for using Basic Calculator v1.0 Developed by Kirklen Allen. Farewell! :D")
                break

            if select not in range(1, 5):
                print("Invalid Input please select a number from 1 to 5")
                continue

            number1 = float(input("Enter first number: "))
            number2 = float(input("Enter second number: "))

            if select == 1:
                print(add(number1, number2))
            elif select == 2:
                print(subtract(number1, number2))
            elif select == 3:
                print(multiply(number1, number2))
            elif select == 4:
                print(divide(number1, number2))
            elif select == 5:
                print(math.sqrt(number1))
        #Exception blocks are used when an error occurs during a program when there is an attempt to create something that doesn't exist.
        #Try-except blocks catch invalid inputs, ensuring the program doesn’t crash.
        except ValueError:
            print("Invalid Input please use numbers")

if __name__ == "__main__":
            calculator()

