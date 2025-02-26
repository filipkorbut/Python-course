#Compound interest calculator

investment = -1
rate = -1
time = -1
while investment < 0 and rate < 0 and time < 0:
    investment = float(input("Enter the amount of money to invest: "))
    rate = float(input("Enter the investment rate: "))
    time = float(input("Enter how long will the interest last: "))
    if investment < 0 or rate < 0 or time < 0:
        print("Please enter only positive values")
total = investment * (1 + rate / 100) ** time
print(f"Your total is: ${total:,.2f}")


