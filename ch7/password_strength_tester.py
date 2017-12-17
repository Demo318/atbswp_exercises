#! /usr/bin/env python3
# Use regular expressions to test the strenght of a password.
# Passwords must have one lowercase letter, capital letter, numeral, symbol,
# and be at least eight characters long.

import re

def test_password():
    """
    Function to test if password meets all requirements.
    Provide user with feedback on what's missing.
    """
    password = input('Please enter a password:')
    missing_items = []

    if not lower_case_ltr(password):
        missing_items.append('lowercase letter')
    if not upper_case_ltr(password):
        missing_items.append('uppercase letter')
    if not digit(password):
        missing_items.append('digit')
    if not symbol(password):
        missing_items.append('symbol')

    if missing_items > 0:
        print("Your password is missing:")
        for i in enumerate(missing_items):
            print(str(i[1]))
    else:
        print("Your password has good complexity.")

    if not length(password):
        print("Your password needs to be at least eight characters long.")
    else:
        print("Your password is plenty long enough.")

def lower_case_ltr(text):
    """Checks string to see if it contains a lowercase letter."""
    lcl_regex = re.compile("[a-z]")
    if lcl_regex.search(text):
        return True
    else:
        return False

def upper_case_ltr(text):
    """Checks string to see if it contains an uppercase letter."""
    ucl_regex = re.compile("[A-Z]")
    if ucl_regex.search(text):
        return True
    else:
        return False

def digit(text):
    """Checks string to see if it contains a digit."""
    d_regex = re.compile(r"\d")
    if d_regex.search(text):
        return True
    else:
        return False

def symbol(text):
    """Checks string to see if it contains a symbol."""
    s_regex = re.compile(r"\D\W\S")
    if s_regex.search(text):
        return True
    else:
        return False

def length(text):
    """checks string to see if it is at least eight carachters long."""
    if len(text) < 8:
        return False
    else:
        return True


test_password()
