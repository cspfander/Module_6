"""
Program: string_functions.py
Author: Colten Pfander
Last date modified: 9/30/2019

The purpose of this program is to take a string (message) and a number (n) and return the string with message printed
n times

    :param message: a string to be printed
    :param n: number of times to print message
    :returns: message printed n number of times
"""


def multiply_string(message, n):
    return message * n


if __name__ == '__main__':
    print(multiply_string("Colten", 4))
