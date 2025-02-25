# Format specifiers = {value:flags} format a value based on what flags are inserted

# .(number) - round to that many decimal places
# :(number) - allocate that many spaces
# :03 - allocate that many spaces
# :< 0 - left justify
# :> 0 - right justify
# :^ 0 - center align
# :+ - use a plus sign to indicate positive value
# := - place sign to leftmost position
# : - insert a space before positive numbers
# :, - comma separator

price1 = 3.14159
price2 = -987.65
price3 = 120000000.34

print(f"Price 1 is ${price1:.2f}")
print(f"Price 2 is ${price2:<010}")
print(f"Price 3 is ${price3:,}")