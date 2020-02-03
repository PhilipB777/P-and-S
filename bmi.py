# This program takes height and weight from people
# and calculates their BMI

height = int(input("Enter your Height in cm: "))/100
weight = int(input("Enter your Weight in kg: "))

bmi = round(weight / (height * height))

print("Your BMI is",bmi,)