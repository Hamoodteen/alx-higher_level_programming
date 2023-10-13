#!/usr/bin/python3
def roman_to_int(roman_string):
    units = {'I': 1, 'II': 2, 'III': 3, 'IV': 4, 'V': 5,
             'VI': 6, 'VII': 7, 'VIII': 8, 'IX': 9}
    tens = {'X': 10, 'XX': 20, 'XXX': 30, 'XL': 40, 'L': 50,
            'LX': 60, 'LXX': 70, 'LXXX': 80, 'XC': 90}
    hundreds = {'C': 100, 'CC': 200, 'CCC': 300, 'CD': 400, 'D': 500,
                'DC': 600, 'DCC': 700, 'DCCC': 800, 'CM': 900}
    thousands = {'M': 1000, 'MM': 2000, 'MMM': 3000}
    if roman_string is not str or roman_string is None:
        return 0
    if roman_string in units:
        return units[roman_string]
    if roman_string in tens:
        return tens[roman_string]
    if roman_string in hundreds:
        return hundreds[roman_string]
    if roman_string in thousands:
        return thousands[roman_string]
