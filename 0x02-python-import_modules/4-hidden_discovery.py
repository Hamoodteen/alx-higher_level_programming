#!/usr/bin/python3
import hidden_4
for str in dir(hidden_4):
    if str[:2] != "__":
        print("{:s}".format(str))
