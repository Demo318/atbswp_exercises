#! /usr/bin/env python3
# pylint: disable=no-member
# Create own version of 'strip' method using regexp.

"""Exercise from ch7 of How to Automate the Boring Stuff in Python."""

import re

def my_strip(usrstring, chars=" "):
    """Method to copy functionality of strip() built-in string method."""

    # identify special characters in chars variable
    chars_list = list(chars)
    special_chars_reg = re.compile(r"\W")
    for i, j in enumerate(chars_list):
        if special_chars_reg.search(j):
            chars_list[i] = '\\' + j

    # Take chars to create regex.
    chars_with_pipes = "|".join(chars_list)
    regex = re.compile(chars_with_pipes)

    # Start from beginning, find first character that doesn't match chars
    pos_index = 0
    for i, j in enumerate(list(usrstring)):
        if regex.search(j):
            pos_index = i + 1
        else:
            break

    # Start from end, find first character that doesn't match chars
    neg_index = None
    for i, j in enumerate(list(reversed(usrstring))):
        if regex.search(j):
            neg_index = -i - 1
        else:
            break

    # Return updated string with characters removed.
    final_string = usrstring[pos_index:neg_index]
    return final_string

print("Tests:")
print(str(my_strip("  test  ") == "test"))
print(str(my_strip("...test...", ".") == "test"))
print(str(my_strip("awsdtestawsd", "awsd") == "test"))
print(str(my_strip("sdtestaw", "awsd") == "test"))
