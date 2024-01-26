#!/usr/bin/python3
"""commenttttttttttttttttttttttttttttttt"""


if __name__ == "__main__":
    import urllib.request
    import urllib.parse
    from sys import argv
    url = argv[1]
    vars = {'email': argv[2]}
    email = urllib.parse.urlencode(vars)
    email = email.encode('utf-8')
    req = urllib.request.Request(url, email)
    with urllib.request.urlopen(req) as response:
        print(response.read().decode("utf-8", "replace"))
