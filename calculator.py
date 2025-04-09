"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
import math

# First example
# santiago changes
def add(a, b):
    return a + b

# my changes
def sub(a, b):
    return a - b

# santiago changes
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



