import time
from math import floor

#wait 2 seconds and then print
#time.sleep(2)
print("Python")

my_time = int(input("Enter a number of seconds: "))

for x in range(my_time, 0, -1):
    secondFormat = x % 60
    minutes = int(x / 60) % 60
    print(f"{minutes:02}:{secondFormat:02}")
    time.sleep(1)
