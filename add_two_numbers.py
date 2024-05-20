#!/usr/bin/python3

"""
This module provides basic mathematical operations.

This module includes a function to add two integers and return their sum.
"""


def add_numbers(number1: int, number2: int) -> int:
    """
    Adds two integers and returns the sum.

    Args:
        number1 (int): The first integer.
        number2 (int): The second integer.

    Returns:
        int: The sum of number1 and number2.

    Example:>>> add_numbers(5, 3)
        8
    """


    return number1 + number2

if __name__ == "__main__":
    num1 = 10
    num2 = 20
    result = add_numbers(num1, num2)
    print(f"The sum of {num1} and {num2} is: {result}")
