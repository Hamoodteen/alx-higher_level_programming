#!/usr/bin/python3
"""commenttttttttttttttttttttttttttttttt"""


if __name__ == "__main__":
    from sys import argv
    import requests as rq
    req = rq.get(argv[1])
    print(req.headers['X-Request-Id'])
