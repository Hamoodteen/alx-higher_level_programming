#!/usr/bin/python3
from calculator_1 import *
from sys import argv, exit
if __name__ == '__main__':
    if len(argv) != 4:
        print("Usage: {} <a> <operator> <b>".format(argv[0]))
        exit(1)
    match argv[2]:
        case "+":
            print("{:d} + {:d} = {:d}".format(argv[1], argv[3], add(argv[1], argv[3])))
        case "-":
            print("{:d} - {:d} = {:d}".format(argv[1], argv[3], sub(argv[1], argv[3])))
        case "*":
            print("{:d} * {:d} = {:d}".format(argv[1], argv[3], mul(argv[1], argv[3])))
        case "/":
            print("{:d} / {:d} = {:d}".format(argv[1], argv[3], div(argv[1], argv[3])))
        case _:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
