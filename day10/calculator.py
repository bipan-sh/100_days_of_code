
#add
from art import logo
import os

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

print(logo)

operations = { '+': add,
               '-': subtract,
               '/': divide,
               '*': multiply,
}

def calculator():
    print(logo)
    num1 = float(input("what's the first number? "))
    should_continue = True

    while should_continue:
        for operators in operations:
            print(operators)
        operation_symbol = input("Pick an operation from the line above: ")
        num2 = float(input("what's the other number? "))
        calculation_symbol = operations[operation_symbol]
        answer = calculation_symbol(num1, num2)

        print(f"{num1} {operation_symbol} {num2} is {answer}" )

        if input("Enter y to continue or n to exit: ") == 'y':
            should_continue = True
            num1 = answer
        else:
            should_continue = False
            os.system('cls')
            calculator()

calculator()
