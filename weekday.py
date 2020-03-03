# Philip Brady
# Outputs if today is a weekday or a weekend day

import datetime

now = datetime.datetime.now()

if now.weekday() in (5, 6):
    print("It is the weekend, yay!")
else:
    print("Yes, unfortunately today is a weekday.")