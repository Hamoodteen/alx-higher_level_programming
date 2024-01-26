#!/usr/bin/python3
"""commenttttttttttttttttttttttttttttttt"""


if __name__ == "__main__":
    from sys import argv
    import requests as rq
    header = "" if len(argv) == 1 else argv[1]
    data = {'q': header}
    req = rq.post("http://0.0.0.0:5000/search_user", data=data)
    try:
        rj = req.json()
        if not rj:
            print("No result")
        else:
            print("[{}] {}".format(rj.get('id'), rj.get('name')))
    except ValueError:
        print("Not a valid JSON")
