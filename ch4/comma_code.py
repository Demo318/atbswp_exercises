def reasonable_list_str(list):
    new_string = ''
    for i in range(0, len(list)):
        if i < (len(list) - 1):
            new_string += str(list[i]) + ', '
        else:
            new_string = new_string + 'and ' + str(list[i]) + '.'
    print(new_string)
    return new_string

print('Please enter some items.')
print('Simply press return when ready to continue.')

user_input = ' '
user_list = []
while True:
    user_input = str(input())
    if user_input == '':
        break
    else:
        user_list.append(user_input)

reasonable_list_str(user_list)