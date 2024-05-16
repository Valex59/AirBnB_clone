#!/usr/bin/python3
"""
This module provides basic mathematical operations.
"""


def add_numbers(number1: int, number2: int) -> int:
    """
    Adds two integers and returns the result.

    Args:
    number1 (int): The first number.
    number2 (int): The second number.

    Returns:
        int: The sum of number1 and number2.
    """
    return number1 + number2


if __name__ == "__main__":
    num1 = 10
    num2 = 20
    result = add_numbers(num1, num2)
    print(f"The sum of {num1} and {num2} is: {result}")
