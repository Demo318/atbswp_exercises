#! /usr/bin/env python3
# Create own version of 'strip' method using regexp.



import re

def my_strip(usrstring, chars = " "):
    """Method to copy functionality of strip() built-in string method."""

    # identify special characters in chars variable
    chars_list= list(chars)
    special_chars_reg = re.compile(r"\W")
    for i, c in enumerate(chars_list):
        if special_chars_reg.search(c):
            chars_list[i] = '\\' + c


    # Take chars to create regex.

    chars_with_pipes = "|".join(chars_list)
    regex = re.compile(chars_with_pipes)


    # Loop from beginning of string
    # Store index from beginning
    # When matches no longer found, break loop & delete indeces that were matched.
    pos_index = 0
    for i, x in enumerate(list(usrstring)):
        if regex.search(x):
            pos_index = i + 1
        else:
            break
   
    # Loop from end of string, counting down i.e. -1, -2, etc.
    # Store index as negative value. 
    # When matches no longer found, break loop & delte indeces that were matched.
    neg_index = None
    for i,x in enumerate(list(reversed(usrstring))):
        if regex.search(x):
            neg_index = -i - 1
        else:
            break

    # Return updated string with characters removed.

    final_string = usrstring[pos_index:neg_index]
    return(final_string)

print("Tests:")
print(str(my_strip("  test  ") == "test"))

print(str(my_strip("...test...", ".") == "test"))

print(str(my_strip("awsdtestawsd", "awsd") == "test"))

print(str(my_strip("sdtestaw", "awsd") == "test"))
