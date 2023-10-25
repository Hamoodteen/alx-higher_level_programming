#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        a = fct(*args)
    except Exception as e:
        sys.stderr.write("Exception: {e}\n".format(e))
        return None
    return a
