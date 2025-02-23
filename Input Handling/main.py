#Input Handling
#input() - A function that prompts the user to enter data. Returns the data as a string

age = int(input("How old are you?   "))

if age < 18:
    print("You are not of age")
else:
    print("You are of age")

#Exercise 1 Rectangle are calculator

length = float(input("Enter the length of a rectangle"))
width = float(input("Enter the width of a rectangle"))

area = length * width
print("The area is", area)

#Exercise 2 Shopping cart

price = float(input("How much is your item?: "))
quantity = int(input("How many do you want to buy?: "))

cost = price * quantity

print("The cost is $", cost)