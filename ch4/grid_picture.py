grid = [['.', '.', '.', '.', '.', '.'], #0
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']] #8

#max X value
x_value = len(grid)
#max Y value
y_value = len(grid[0])

for i in range(y_value):
    str_row = ''
    for j in range(x_value):
        str_row += grid[j][i]
    print(str_row)
