#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or not isinstance(roman_string, str):
        return 0
    roman_numbers = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    sum = 0
    prev_val = 1000
    for ch in roman_string:
        if ch in roman_numbers:
            if roman_numbers[ch] <= prev_val:
                sum += roman_numbers[ch]
            else:
                sum = roman_numbers[ch] - sum
            prev_val = roman_numbers[ch]
    return sum
