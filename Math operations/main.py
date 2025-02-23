import math # import the math lib

# number = 0
# # number += 1
# # number -= 1
# # number *= 2
# # number /= 2
# # number **=  2 #To the power of 2
# number %= 2
#
# print(number)
#
# # round() - rounds the number. Can also limit the number of decimal points: round(number, 2)
# print(round(3.2)) # out: 3
# print(round(3.5)) # out: 4
#
# # abs() - distance away from 0 as a number
# print(abs(-10)) # out: 10
#
# # pow()
# pow(2, 4)
#
# # min() and max() return the minimum and maximum value respectively
# min(2,4,5) # out: 2
# max(2,4,5) # out: 5
#
# # Math
# print(math.ceil(3.2))
# print(math.floor(3.2))
# print(math.pi)
# print(math.e)

# Exercise 1 - Calculate the circumference of a circle (2PI * r)
radius = float(input("Enter the radius of the circle: "))
circumference = 2 * math.pi * radius
print("Circumference of the circle: ", round(circumference, 2))

# Exercise 2 - Calculate the area of a circle (PI * r * r)
radius = float(input("Enter the radius of the circle: "))
area = math.pi * pow(radius, 2)
print("Area of the circle: ", round(area, 2))