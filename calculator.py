"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
import math

# First example
def add(a, b):
    return a + b
def subtract(a,b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    if a == 0:
        raise ZeroDivisionError
    else:
        return b / a
def logarithm(a,b):
    try:
        return math.log(a,b)
    except ValueError:
        return None
def exponent(a, b):
    try:
        return math.exp(a,b)
    except ValueError:
        return None



