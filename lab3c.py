#!/usr/bin/env python3
'''Lab 3 Inv 2 function operate'''
# Author ID: mepalaypay1

def operate(number1, number2, operator):
    number1 = int(number1)
    number2 = int(number2)

    if operator == 'add':
        return number1 + number2
    elif operator == 'subtract':
        return number1 - number2
    elif operator == 'multiply':
        return number1 * number2
    else:
        return 'Error: function operator can be "add", "subtract", or "multiply"'

if __name__ == '__main__':
    print(operate(10, 5, 'add'))
    print(operate(10, 5, 'subtract'))
    print(operate(10, 5, 'multiply'))
    print(operate(10, 5, 'divide'))