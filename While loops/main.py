# while loop - execute code while condition remains true


name = input("Enter your name: ")
while name == "":
    print("Please enter your name: ")
    name = input()
print("Hello, " + name)

# while not works the same as '!='

food = input("Enter food (q to quit): ")
while not food == "q":
    print(f"Your food is: {food}")
    food = input("Enter food (q to quit): ")
print("Exited")

# Exercise 1 - Create a program that prints every number from 1-n

n = int(input("Enter your number: "))
i = 1
while i <= n:
    print(f"{i} ")
    i += 1