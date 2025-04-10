# https://github.com/sotoya99/lab10-SO-CH
# Partner 1: Santiago Otoya
# Partner 2: Cher Huang

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
        raise ZeroDivisionError("error: divide by zero")
    else:
        return b / a
def exp(a, b):
    return a ** b

def logarithm(a,b): # you will get an error for this (the the log test case should pass once you fix this). Good luck! ^-^
    try:
        return math.log(a,b)
    except ValueError:
        return None




