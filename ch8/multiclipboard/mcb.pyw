#! /usr/bin/env python3
# mcb.pyw - Saves and loads pieces of text to the clipboard.
# Usage: py.exe mcb.pyw save <keyword> - Save clipboard to keyword.
#        py.exe mcb.pyw <keyword> - Loads keyword to clipboard.
#        py.exe mcb.pyw list - Loads all keywords to clipboard.
#        py.exe mcb.pyw delete <keyword> - Deletes single item from stored list.
#        py.exe mcb.pyw DELETE ALL - Deletes all key-value pairs stored in shelf.

"""Create keyword for retreiving text."""

import sys
import shelve
import pyperclip


MCB_SHELF = shelve.open('mcb')




if len(sys.argv) == 3:
    # Save clipboard content.
    if sys.argv[1].lower() == 'save':
        MCB_SHELF[sys.argv[2]] = pyperclip.paste()
    # Delete all items from shelf.
    elif sys.argv[1] + sys.argv[2] == 'DELETEALL':
        for key in enumerate(MCB_SHELF.keys()):
            del MCB_SHELF[key[1]]
    # Delete item from saved list.
    elif sys.argv[1].lower() == 'delete':
        del MCB_SHELF[sys.argv[2]]


elif len(sys.argv) == 2:
    # List keywords and load content.
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(MCB_SHELF.keys())))
    elif sys.argv[1] in MCB_SHELF:
        pyperclip.copy(MCB_SHELF[sys.argv[1]])


MCB_SHELF.close()
