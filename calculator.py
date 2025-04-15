"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""

# https://github.com/jaipat30/lab10-JP-PP
# Partner 1: Paul Pham
# Partner 2: [Your Partner's Name]

import math

def square_root(x):
    if x < 0:
        raise ValueError("Cannot take square root of a negative number")
    return math.sqrt(x)

def absolute(x):
    return abs(x)

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if a == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return b / a

def logarithm(a, b):
    if a <= 0 or a == 1 or b <= 0:
        raise ValueError("Logarithm base must be > 0 and ≠ 1; input must be > 0")
    return math.log(b, a)

def exponent(a, b):
    return a ** b
    return math.log(b, a)

def exp(a, b):
    return a ** b
