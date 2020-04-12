# Philip Brady
# This program takes in the height and weight from people,
# calculates their BMI and outputs the result.

# The weight is taken in and converted to the int type.
weight = int(input("Enter your Weight in kg: "))
# The  height is taken in and converted to the int type
# before the cm height is divided by 100 to convert it
# to metres.
height = int(input("Enter your Height in cm: "))/100

# The weight is divided by height in metres squared.
# It is rounded to two decimal places.
bmi = round(weight / (height * height), 2)

print("Your BMI is {}.".format(bmi))

# Reference:
# “A Whirlwind Tour of Python by Jake VanderPlas (O’Reilly).
# Copyright 2016 O’Reilly Media, Inc., 978-1-491-96465-1.”