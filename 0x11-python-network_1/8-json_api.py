#!/usr/bin/python3
"""commenttttttttttttttttttttttttttttttt"""


if __name__ == "__main__":
    from sys import argv
    import requests as rq
    header = argv[1] if len(argv) > 1 else ""
    req = rq.post("http://0.0.0.0:5000/search_user", {"q": header})
    try:
        rj = req.json()
        if rj == {}:
            print("No result")
        else:
            rhg = req.headers
            print("[{}] {}".format(rhg.get('id'), rhg.get('name')))
    except ValueError:
        print("Not a valid JSON")
