def collatz(num): #function that will count all the way down to one. No one knows why. Math and stuff.
    if num % 2 == 0:
        num = num // 2
        print(str(num))
        return num
    else:
        num = 3 * num + 1
        print(str(num))
        return num

#loop to get user input
while 1 == 1:
    try:
        user_num = int(input('Enter a number:\n'))
    except ValueError:
        print('Please enter a number')
        continue
    break

while user_num > 1:
    user_num = collatz(user_num)
