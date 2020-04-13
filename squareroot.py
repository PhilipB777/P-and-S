# Philip Brady
# This is the Weekly Task 6.
# The program takes a positive floating-point
# number as input and outputs an approximation
# of its square root.  The function called sqrt
# does this.

# Imported the math module.
import math

# Created a function that takes the value x.
def sqrt(x):
    # Used the sqrt function of the math module.
    # Rounded answer to one decimal place.
    answer = round(math.sqrt(x),1)
    return answer

# Created the variable number which would be
# assigned the inputted floating point number.
number = float(
input("Please enter a positive number: "))

# Called the sqrt function from the print function.
print("The square root of {} is approx. {}."
.format(number, sqrt(number)))

# References:
# [1]  “A Whirlwind Tour of Python by Jake VanderPlas (O’Reilly).
# Copyright 2016 O’Reilly Media, Inc., 978-1-491-96465-1.”
# [2]  https://docs.python.org/3/library/math.html