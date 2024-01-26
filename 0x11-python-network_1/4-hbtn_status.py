#!/usr/bin/python3
"""commenttttttttttttttttttttttttttttttt"""


if __name__ == "__main__":
    import requests as rq
    req = rq.get("https://alx-intranet.hbtn.io/status")
    print("Body response:")
    rutf = req.content.decode("utf-8", "replace")
    print("\t- type: {}".format(type(rutf)))
    print("\t- content: {}".format(rutf))
