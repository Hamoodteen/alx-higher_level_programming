#!/usr/bin/python3
"""commenttttttttttttttttttttttttttttttt"""


if __name__ == "__main__":
    from sys import argv
    import requests as rq
    headers = {'email': argv[2]}
    req = rq.post(argv[1], headers=headers)
    print("Your email is: {}".format(req.headers.get('email')))
