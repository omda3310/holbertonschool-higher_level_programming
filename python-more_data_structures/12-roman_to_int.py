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
    for ch in range(len(roman_string)):
      if ch >0 and roman_numbers[roman_string[ch]] > roman_numbers[roman_string[ch -1]]:
          sum += roman_numbers[roman_string[ch]] - 2 * roman_numbers[roman_string[ch -1]]
    else:
        sum += roman_numbers[roman_string[ch]]
    return sum
