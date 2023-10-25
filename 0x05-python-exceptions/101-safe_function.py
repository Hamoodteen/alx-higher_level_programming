#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        return fct
    except Exception as e:
        sys.stderr.write("Exception: {e}\n".format(e))
        return None
