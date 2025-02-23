# if-else statements

# Exercise 1 - Check if a number is positive, negative, or zero
# Write a Python program that takes a number as input and prints whether it is positive, negative, or zero.

number = 4
if number < 0:
    print ("Number is negative")
elif number == 0:
    print ("Number is zero")
else:
    print("Number is positive")

# Exercise 2 - Determine if a number is even or odd
# Write a Python program that asks the user for a number and determines if it is even or odd.

input = int(input("Enter a number"))
if input%2 == 0:
    print ("Number is even")
else:
    print ("Number is odd")

# Shortened version
a = 1
b = 2
min_num = a if a < b else b
max_num = a if a > b else b