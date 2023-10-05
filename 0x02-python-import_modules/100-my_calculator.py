#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
from sys import argv, exit
if __name__ == '__main__':
    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    match argv[2]:
        case "+":
            print("{:d} + {:d} = {:d}".format(argv[1], argv[3], add(int(argv[1]), int(argv[3]))))
        case "-":
            print("{:d} - {:d} = {:d}".format(argv[1], argv[3], sub(int(argv[1]), int(argv[3]))))
        case "*":
            print("{:d} * {:d} = {:d}".format(argv[1], argv[3], mul(int(argv[1]), int(argv[3]))))
        case "/":
            print("{:d} / {:d} = {:d}".format(argv[1], argv[3], div(int(argv[1]), int(argv[3]))))
        case _:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
