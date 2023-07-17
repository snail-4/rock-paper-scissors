import random
choices = ('s', 'r', 'p')
pc = random.choice(choices)
user_choice =input('Your move: (r, p or s)')

counter1 = 0
counter2 = 0
while counter1 < 3 and counter2 < 3:
    pc = random.choice(choices)
    if user_choice == 'r' and pc == 's':
        print(f'PC choice: {pc}\nYou won!')
        counter1 = counter1 + 1
        print('you -', counter1)
        print('pc -', counter2)
        user_choice = input('Your move: (r, p or s)')
    elif user_choice == 's' and pc == 'p':
        print(f'PC choice: {pc}\nYou won!')
        counter1 = counter1 + 1
        print('you -', counter1)
        print('pc -', counter2)
        user_choice = input('Your move: (r, p or s)')
    elif user_choice == 'p' and pc == 'r':
        print(f'PC choice: {pc}\nYou won!')
        counter1 = counter1 + 1
        print('you -', counter1)
        print('pc -', counter2)
        user_choice = input('Your move: (r, p or s)')
    elif user_choice == 'r' and pc == 'p':
        print(f'PC choice: {pc}\nYou lost!')
        counter2 = counter2 + 1
        print('you -', counter1)
        print('pc -', counter2)
        user_choice = input('Your move: (r, p or s)')
    elif user_choice == 'p' and pc == 's':
        print(f'PC choice: {pc}\nYou lost!')
        counter2 = counter2 + 1
        print('you -', counter1)
        print('pc -', counter2)
        user_choice = input('Your move: (r, p or s)')
    elif user_choice == 's' and pc == 'r':
        print(f'PC choice: {pc}\nYou lost!')
        counter2 = counter2 + 1
        print('you -', counter1)
        print('pc -', counter2)
        user_choice = input('Your move: (r, p or s)')
    elif user_choice == pc:
        print(f'PC choice: {pc}\nDraw!')
        print('you -', counter1)
        print('pc -', counter2)
        user_choice = input('Your move: (r, p or s)')

def winner(counter1, counter2):
    if counter1 == 3:
        print('You won!')
        return counter1
    elif counter2 == 3:
        print('You lost!')
        return counter2

winner(counter1,counter2)