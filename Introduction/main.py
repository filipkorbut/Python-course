print("Hello World!")

#Variables

#String
name = "John"
last_name = "Smith"
print(f"Hello {name}, {last_name}")

#Integer
age = 30
quantity = 5
print(age, quantity)

#Float
pi = 3.14
radius = 2.5
print(f"pi = {pi}, radius = {radius}")

#Boolean
isTrue = False
isFalse = True

#If else statements
if isTrue:
    print("True")
else:
    print("False")

#Type casting. int(), str(), float(), bool()

number = 5
float = 2.4

#When casting from an integer, it cuts away the decimal portion
print(int(float))

#type(var) returns the type of variable
print(type(number))