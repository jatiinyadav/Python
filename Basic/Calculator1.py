# Calculator

from calculatorif import *


def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    return x / y


if(choice <= 4):
    One = float(input("Enter 1st Number: "))
    Two = float(input("Enter 2nd Number: "))
    if choice == 1:
        result = add(One, Two)
        print(result)
    elif choice == 2:
        result = subtract(One, Two)
        print(result)
    elif choice == 3:
        result = multiply(One, Two)
        print(result)
    elif choice == 4:
        result = divide(One, Two)
        print(result)
else:
    print("Please Enter Valid Choice")
