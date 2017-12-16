#! /usr/bin/env python3
# Fantasy game inventory exercise from 'Automate the Boring Stuff with Python' ch.5
# https://automatetheboringstuff.com/chapter5/

# Create one function to display an inventory (stored as a dictionary, str:int pairs).
# Create another function to take a list and add to the player's inventory.


# Display items in player's inventory.
# Single argument = dictionary of items.
def display_inventory(inventory):
    total_items = 0

    print("Inventory:")
    for item, count in inventory.items():
        total_items += count
        print(f"{item}: {count}")
    print(f"Total number of items: {total_items}")

test_inventory = {"sword":1, "knife": 1, "apples":10}
display_inventory(test_inventory)


# Add items to player's inventory.
# Arg1 = dictionary of player's items
# Arg2 = list of new items
def add_items(inventory, new_items):
    for i in new_items:
        inventory.setdefault(i, 0)
        inventory[i] += 1
    display_inventory(inventory)


found_items = ['flask', 'backpack', 'health potion', 'sword']
add_items(test_inventory, found_items)
