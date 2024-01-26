#!/usr/bin/python3
"""commenttttttttttttttttttttttttttttttt"""


if __name__ == "__main__":
    import urllib.request as urlr
    import urllib.error as urle
    from sys import argv
    try:
        with urlr.urlopen(argv[1]) as response:
            html = response.read()
            print(html)
    except urle.HTTPError as error:
        print("Error code: {}".format(error.code))
