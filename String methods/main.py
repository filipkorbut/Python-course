name = input("Enter your name: ")

print(len(name))
print(name.find(" "))
print(name.rfind(" "))
print(name.capitalize())
print(name.upper())
print(name.lower())
print(name.isdigit())
print(name.isalpha())

#Exercise 1 - Validate user input
#must not contain any spaces
#must be up to 12 characters long

username = input("Enter your username: ")

if len(username) < 12:
    print("Your username is too short")
elif not  username.find(" "):
    print("Your username can't contain spaces")
else:
    print(f"Welcome {username}")