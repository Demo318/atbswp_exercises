tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

def print_table(table):
    column_widths = find_column_widths(table)
    table = reformat_items(table, column_widths)
    for i in table:
        print('  '.join(i))
    

def find_column_widths(table):
    max_widths = [0]* len(table[0])

    for i in range(len(table)):
        for j in range(len(table[i])):
            temp_width = len(table[i][j])
            current_width = max_widths[j]
            if temp_width > current_width:
                max_widths[j] = temp_width
    return max_widths


def reformat_items(table, widths):
    for i in range(len(table)):
        for j in range(len(table[i])):
            table[i][j] = table[i][j].ljust(widths[j])
    return table


print_table(tableData)