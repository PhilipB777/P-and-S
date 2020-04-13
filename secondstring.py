# Philip Brady
# This is the Weekly Task 3.
# The program takes in a sentence from
# the user and outputs every second
# letter in reverse order.

sen = input("Please enter a sentence: ")

# Used the string slicing required within
# the print function.
print("Every 2nd letter in reverse is {}"
.format(sen[::-2]))