#!/usr/bin/python3
def fizzbuzz():
    for i in range(1, 101):
        print("{}".format(i if i % 3 != 0 else "FizzBuzz"), end="")
