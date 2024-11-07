"""
File Name: calculator.py
Author: Samuel Jeffman
Date: 2024-11-07
Description: Programming in Python: Basic and Preparatory Course, Assignment 2. Simple calculator app.
"""

# Import math library
import math

# Add two numbers
def add(x1, x2):
    return x1+x2

# Subtract two numbers
def subtract(x1, x2):
    return x1-x2

# Multiply two numbers
def multiply(x1, x2):
    return x1*x2

# Divide two numbers
def divide(x1,x2):
    return x1/x2

# Calculate the hypotenuse of the two provided numbers
def hypotenuse(a, b):
    c = math.sqrt(a**2 + b**2)
    return c

def pow(x,y):
    return x**y

# Only run the code below if this is the main .py file
if __name__ == "__main__":
    #The input function reads a line, and the program converts the entire line to a floating point
    #number. Test entering two numbers on the same line. What goes wrong?
    #### Input is interpreted as text and converted to a 'string', Type converting a 'string' to a 'float' doesn't work.

    print("Enter two numbers:")

    # Read input as floats
    x1 = float(input())
    x2 = float(input())
    #print(x1, '+', x2, '=', x1+x2)

    print('What operation should we perform on these numbers? Enter: +, -, *, / or hyp')

    # Read input as string to decide what to do
    opr = str(input())

    # Print the different results depending on what operation was selected.
    if(opr == '+'):
        print(f"Result of {x1}+{x2} is",add(x1,x2),end='\n')
    elif(opr == '-'):
        print(f"Result of {x1}-{x2} is",subtract(x1,x2),end='\n')
    elif(opr == '*'):
        print(f"Result of {x1}*{x2} is",multiply(x1,x2),end='\n')
    elif(opr == '/'):
        print(f"Result of {x1}/{x2} is",divide(x1,x2),end='\n')
    elif(opr == 'hyp'):
        print(f"Hypotenuse of {x1} and {x2} is: ",round(hypotenuse(x1,x2),2),end='\n')
        #NameError: name 'a' is not defined
        #Variable 'a' doesn't exist in this scope
        #print(a)
        #NameError: name 'c' is not defined
        #Variable 'c' doesn't exist in this scope
        #print(c)
    else:
        print(f"Invalid operation: '{opr}'")