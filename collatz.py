# Philip Brady
# This is the Weekly Task 4.
# The program takes in any positive integer
# and outputs the successive values of the
# following calculation:
# At each step the next value is calculated
# by taking the current value and if it is
# even, divide it by two, but if it's odd,
# multiply it by three and add one. The
# program ends if the current value is one.

# Take in the integer and assign it to result.
result = input("Please enter a positive integer: ")
# Convert to int type and assign it to number.
number = int(result)

# Initialise a while loop which continues until
# the number is equal to 1.
while number != 1:
    # Check if number is even.
    if number % 2 == 0:
        # Calculation for even number.
        number = number/2
    else:
        # Calculation for odd number.
        number = (number*3) + 1
    # Concatenate each value to the result string.
    # This keeps the values on one line.
    result = result + " " + str(round(number))
print("The successive values are {}.".format(result))

# Reference:
# “A Whirlwind Tour of Python by Jake VanderPlas (O’Reilly).
# Copyright 2016 O’Reilly Media, Inc., 978-1-491-96465-1.”