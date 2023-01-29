import json
import random
import string

def load_data():
    json_data = []
    with open('data.json') as json_file:
        json_data = json.load(json_file)

    return json_data

# print(json_data)

def get_valid_words(words):
    word = random.choice(words) # randomly chooses something from the list
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word

def hangman():
    words = load_data()
    # print(f'length of list: {len(words)}')
    word = get_valid_words(words)
    word_letters = set(word)    # letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set()    # what user has guessed

    # get user input 
    while len(word_letters) > 0:
        # letters used
        print('You have used these letters: ',''.join(used_letters))

        # what currently word is (e.g. W - R D)
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word: ',''.join(word_list))

        user_input_letter = input('Guess a letter: ').upper()
        if user_input_letter in alphabet - used_letters:
            used_letters.add(user_input_letter)
            if user_input_letter in word_letters:
                word_letters.remove(user_input_letter)

        elif user_input_letter in used_letters:
            print("You've already used that letter. Please try again.")

        else:
            print("Invalid letter. Please try again.")

hangman()