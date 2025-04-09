"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
import math

# First example
def square_root(a):
    if a < 0:
        raise ValueError
    else:
        return math.sqrt(a)

def hypotenuse(a, b):
    return math.hypot(a, b)

def add(a, b):
    return a + b
def subtract(a,b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if a == 0:
        raise ZeroDivisionError
    else:
        return b / a
def exp(a, b):
    try:
        return math.exp(a,b)
    except ValueError:
        return None
def logarithm(a,b):
    try:
        return math.log(a,b)
    except ValueError:
        return None




