"""Does this count as the module docstring?"""

TABLE_DATA = [['apples', 'oranges', 'cherries', 'banana'],
              ['Alice', 'Bob', 'Carol', 'David'],
              ['dogs', 'cats', 'moose', 'goose']]

def print_table(table):
    """Print 2-dimensional array with all items evenly organized into columns"""
    column_widths = find_column_widths(table)
    table = reformat_items(table, column_widths)
    for i in table:
        print('  '.join(i))
    return True

def find_column_widths(table):
    """Identify the longest string length for each column."""
    max_widths = [0]* len(table[0])

    for i in enumerate(table):
        for j, k in enumerate(table[i[0]]):
            temp_width = len(k)
            current_width = max_widths[j]
            if temp_width > current_width:
                max_widths[j] = temp_width
    return max_widths


def reformat_items(table, widths):
    """Add white space so every string in column has same length."""
    for i in enumerate(table):
        for j, k in enumerate(table[i[0]]):
            table[i[0]][j] = k.ljust(widths[j])
    return table


print_table(TABLE_DATA)
