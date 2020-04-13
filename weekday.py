# Philip Brady
# This is the Weekly Task 5.
# The program outputs whether or not today is a
# week day or a weekend day.

# The datetime module is imported.
import datetime

# The datetime.now() function returns various
# attributes of the the present date and time.
now = datetime.datetime.now()

# The weekday function returns the day of the week
# as an integer, where Monday is 0 and Sunday is 6.
if now.weekday() in (5, 6):
    print("It is the weekend, yay!")
else:
    print("Yes, unfortunately today is a weekday.")

# References:
# [1]  “A Whirlwind Tour of Python by Jake VanderPlas (O’Reilly).
# Copyright 2016 O’Reilly Media, Inc., 978-1-491-96465-1.”
# [2]  https://docs.python.org/3/library/datetime.html