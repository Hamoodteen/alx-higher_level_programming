#!/usr/bin/python3
"""commenttttttttttttttttttttttttttttttt"""


if __name__ == "__main__":
    from sys import argv
    import requests as rq
    from requests.auth import HTTPBasicAuth
    auth = HTTPBasicAuth(argv[1], argv[2])
    r = rq.get('https://api.github.com/user', auth=auth)
    if r.status_code == 200:
        rj = r.json()
        print(rj.get('id'))
    else:
        print(None)
