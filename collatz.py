# Philip Brady
# This is the Weekly Task 4

result = input("Enter positive integer: ")
number = int(result)

while number != 1:
    if number % 2 == 0: 
        number = number = number/2
    else:
        number = (number*3) + 1
    result = result + " " + str(round(number))
print(result)