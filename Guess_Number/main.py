import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f'Guess a number between 1 and {x}: '))
        if guess < random_number:
            print('Sorry, guess again. Too low.')
        elif guess > random_number:
            print('Sorry, guess again. Too high.')
    print(f'Wow Chodya! you guessed right: {guess}')


def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            # print(f'l: {low}, h: {high}')
            guess = random.randint(low , high)
        else: 
            guess = low # could also be high since low == high
        feedback = input(f'Is {guess} too high (H), too low (L), or correct (C)?? ').lower()
        if feedback == 'h':
            # print('too high, updaing higher bounds')
            high = guess - 1
        elif feedback == 'l':
            # print('too low, updateing lower bounds')
            low = guess + 1
    print(f'Yay chodya you guess my number correctly: {guess}')


computer_guess(100)