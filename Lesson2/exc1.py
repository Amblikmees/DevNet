numbers = [5, 6, 8, 9, 22, 66, 33, 88]
print("My list is " + str(numbers))

for number in numbers:
    if number > 10:
        print("The number is over 10!")
    elif number == 10:
        print("The number is 10!")
    else:
        print("Small number")
