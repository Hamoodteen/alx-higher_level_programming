#!/usr/bin/python3
"""commenttttttttttttttttttttttttttttttt"""


if __name__ == "__main__":
	import urllib.request


	with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as response:
		html = response.read()
