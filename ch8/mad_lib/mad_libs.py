#! /usr/bin/env python3
# Fantasy game inventory exercise from 'Automate the Boring Stuff with Python' ch.5
# https://automatetheboringstuff.com/chapter8/

import re
import random


# Define regex for extracting madlib info.
lib_regex = re.compile(r'(\[)(.+)(\]\[)(.+)(\])', re.DOTALL)

# Declare empty list to record which mad libs a player has already used.
already_used_libs = []

# Read from a text file to randomly import a Mad Lib
libs_file = open('mad_libs.txt', 'r')

libs = []
for line in enumerate(libs_file.readlines()):
    if not re.search(r'^--', line[1]):
        libs.append(line[1])

# Recursive method to find 
def find_random_number(max, history):
    rand_int = random.randint(0, max)
    while rand_int in history:
        find_random_number(max, history)
    return rand_int

# Clear already_used_libs list if player has already gone through
# the entire inventory.
if len(libs) == len(already_used_libs):
    already_used_libs = []

# Use find_random_number to determine which madlib is next.
lib_ind = find_random_number(len(libs) - 1, already_used_libs)

# Record randomly generated lib_ind to madlib already-used history.
already_used_libs.append(lib_ind)

# Create regex object.
regd_lib = lib_regex.search(libs[lib_ind])

# Separate the madlib string from the input needed from user.
lib_string = regd_lib.group(2)
lib_words = regd_lib.group(4).split(", ")

# Record user-entries for variable fields.
user_entries = []
for word in enumerate(lib_words):
    print("Please enter a {}:".format(word[1]))
    user_entries.append(input())

# Print string back to the console for user.
print(lib_string.format(*user_entries).replace('\\n','\n'))


# TODO: Package code in a loop so player can keep playing.
