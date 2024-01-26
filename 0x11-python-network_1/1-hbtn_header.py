#!/usr/bin/python3
"""commenttttttttttttttttttttttttttttttt"""


if __name__ == "__main__":
    import urllib.request
    from sys import argv
    url = argv[1]
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as response:
        head = response.getheader('X-Request-Id')
        print(head)
