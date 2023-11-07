#!/usr/bin/python3
"""commentttttttttttttttttttttttttttt"""


if __name__ == "__main__":
    import sys
    save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
    load_from_json_file = __import__("6-load_from_json_file").load_from_json_file


"""commentttttttttttttttttttttttttttt"""
try:
    ls = load_from_json_file("add_item.json")
except FileNotFoundError:
    ls = []
for i in sys.argv[1:]:
    ls.append(i)
save_to_json_file(ls, "add_item.json")
