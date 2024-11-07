"""
File Name: distance.py
Author: Samuel Jeffman
Date: 2024-11-07
Description: Programming in Python: Basic and Preparatory Course, Assignment 2. Simple distance calculator app, using imported functions.
"""

# Import calculator functions provided in a separate file, calculator.py
from calculator import *

# Calculate distance between two sets of coordinates.
def distance(x1,x2,y1,y2):
    x = subtract(x2,x1)
    y = subtract(y2,y1)
    return hypotenuse(x,y) # hypotenuse is defined in calculator.py

# Read input
print('Enter coordinates:\nx1:')
x1 = float(input())
print('x2:')
x2 = float(input())
print('y1:')
y1 = float(input())
print('y2:')
y2 = float(input())

# Print result
print(f'Distance between coordinates is {distance(x1,x2,y1,y2)}')