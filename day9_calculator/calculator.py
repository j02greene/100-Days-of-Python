from art import logo
import os
import platform

def clear():
    if platform.system() == 'Linux':
        os.system('clear')
    elif platform.system() == 'Windows':
        os.system('cls')

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operation_dictionary = {

"+": add,
"-": subtract,
"*": multiply,
"/": divide

}
def calculator():
    print(logo)

    do_continue = True

    num1 = int(input("What is the first number?: "))
    for operation in operation_dictionary:
        print(operation)

    while do_continue:


        operation_choice = input("Pick an operation from above: ")

        num2 = int(input("What is the next number?: "))

        calculation = operation_dictionary[operation_choice]

        answer = calculation(num1, num2)

        print(f"{num1} {operation_choice} {num2} = {answer}")
        keep_calculating = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ")
        if keep_calculating == 'y':
            num1 = answer
        else:
            do_continue = False
            clear()
            calculator()
            


calculator()