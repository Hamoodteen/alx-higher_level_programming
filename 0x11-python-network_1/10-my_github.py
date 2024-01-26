#!/usr/bin/python3
"""commenttttttttttttttttttttttttttttttt"""


if __name__ == "__main__":
    from sys import argv
    import requests as rq
    r = rq.get('https://api.github.com/user', auth=(argv[1], argv[2]))
    print(r.headers.get('id') if r.status_code == 200 else None)
