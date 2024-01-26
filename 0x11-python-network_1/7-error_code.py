#!/usr/bin/python3
"""commenttttttttttttttttttttttttttttttt"""


if __name__ == "__main__":
    import requests as rq
    from sys import argv
    req = rq.get(argv[1])
    if req.status_code >= 400:
        print("Error code: {}".format(req.status_code))
    else:
        rutf = req.content.decode("utf-8", "replace")
        print(rutf)
