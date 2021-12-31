import random

user_wins = 0
computer_wins = 0
options = ['rock', 'paper', 'scissors']

print('Welcome to a game of rock, paper, scissors!')
print('===========================================')

while True:
    print(f'Computer score: {computer_wins}   User score: {user_wins}')

    user_input = input('Type Rock/Paper/Scissors or Q to quit: ').lower()

    if user_input == 'q':
        break

    if user_input not in options:
        continue

    random_number = random.randint(0, 2)
    # rock: 0, paper: 1, scissors: 2
    computer_pick = options[random_number]
    print(f'Computer picked {computer_pick}.')

    if user_input == computer_pick:
        print('It is a tie. Nobody wins!')
    elif user_input == 'rock' and computer_pick == 'scissors':
        print('You won!')
        user_wins += 1
    elif user_input == 'paper' and computer_pick == 'rock':
        print('You won!')
        user_wins += 1
    elif user_input == 'scissors' and computer_pick == 'paper':
        print('You won!')
        user_wins += 1
    else:
        print('You lost!')
        computer_wins += 1

print('\nThank you for playing my game! Goodbye =)')
