#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
num10 = abs(number) % 10
if num10 > 5:
    print(f"Last digit of {number} is {num10} and is greater than 5")
elif num10 < 6 and num10 != 0:
    print(f"Last digit of {number} is {num10} and is less than 6 and not 0")
else:
    print(f"Last digit of {number} is {num10} and is 0")
