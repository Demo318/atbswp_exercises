#! /usr/bin/env python3
# Use regular expressions to test the strenght of a password.
# Passwords must have one lowercase letter, capital letter, numeral, symbol,
# and be at least eight characters long.

import re

def test_password():
    password = input('Please enter a password:')
    missing_items = []

    if not lower_case_ltr(password):
        missing_items += 'lowercase letter'
    if not upper_case_ltr(password):
        missing_items += 'uppercase letter'
    if not digit(password):
        missing_items += 'digit'
    if not symbol(password):
        missing_items += 'symbol'

    if len(missing_items) > 0:
        print("Your password is missing:")
        for i in enumerate(missing_items):
            print(str(i[1]))
        
    


"""Checks string to see if it contains a lowercase letter."""
def lower_case_ltr(text):


"""Checks string to see if it contains an uppercase letter."""
def upper_case_ltr(text):

"""Checks string to see if it contains a digit."""
def digit(text):

"""Checks string to see if it contains a symbol.""""
def symbol(text):

"""checks string to see if it is at least eight carachters long.""""
def length(text):
