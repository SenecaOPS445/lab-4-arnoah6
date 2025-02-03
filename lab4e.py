#!/usr/bin/env python3

# Author ID: arnoah

def is_digits(sobj):
    # Loop through each character in the string
    for char in sobj:
        if not char.isdigit():  # If the character is not a digit
            return False
    return True  # If all characters are digits, return True

if __name__ == '__main__':
    test_list = ['x3058', '3058', '8503x', '8503']
    for item in test_list:
        if is_digits(item):
            print(item, 'is an integer.')
        else:
            print(item, 'is not an integer.')
