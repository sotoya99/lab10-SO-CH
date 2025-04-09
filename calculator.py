"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
import math

# First example

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if a == 0:
        raise ZeroDivisionError
    else:
        return b / a
def log(a,b):
    try:
        return math.log(a,b)
    except ValueError:
        return None
def exp(a, b):
    try:
        return math.exp(a,b)
    except ValueError:
        return None


def add(a, b):
    return a + b

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



