"""
File Name: functions.py
Author: Samuel Jeffman
Date: 2024-11-07
Description: Programming in Python: Basic and Preparatory Course, Assignment 2. Simple unit conversion app, using imported functions.
"""

# Import math library
import math
# Import calculator functions provided in a separate file, calculator.py
from calculator import *

# Convert miles to km
def to_km(miles):
    return divide(
        multiply(1609.344, miles),
        1000)         
    # return (1609.344*miles)/1000

# Convert km to miles
def to_miles(km):
    return divide(
        multiply(km, 1000), 
        1609.344)
    # return (km*1000)/1609.344

# Convert fahrenheit to celsius
def to_celsius(fahrenheit):
    return multiply(
        divide(5,9),
        subtract(fahrenheit,32))
    # return ((5/9) * (f - 32))

# Convert celsius to fahrenheit
def to_fahrenheit(celsius):
    return add(
        multiply(
            divide(9,5), 
            celsius), 
        32)
    # return (((9/5) * c) + 32)

# Calculate area of a circle with the provided diameter
def circle_area(dia):
    return multiply(
        divide(math.pi, 4), 
        pow(dia,2))
    #return (math.pi / 4) * d**2

# Convert and print the provided range of degrees in C to F
def print_c2f_table(from_c, to_c):
    for celsius in range(from_c, to_c + 1): # +1 to make to_c inclusive
        print("C: ",celsius," F:",to_fahrenheit(celsius))
    print('\n')

# Print results
print("\n\n5 miles is", round(to_km(5),2),"km")
print("5 km is", round(to_miles(5),2),"miles")
print("5 C is", round(to_fahrenheit(5),2), "F")
print("5 F is", round(to_celsius(5),2), "C")
print("5 cm is", round(circle_area(5),2), "cm2", end='\n\n')
print_c2f_table(-12,12)