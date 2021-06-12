import random
from random_words import RandomWords
rw = RandomWords()


def get_valid_word(word):
    word = rw.random_word()
    while '-' in word or ' ' in word:
        word = rw.random_word()

    return word


def hangman():
    word = get_valid_word(word)
    word_letters = set(word)  # letters in the word
    alphabet = set(string.ascii.uppercase)  # letters in a set of asci char
    used_letters = set()  # used letters

    while len(word_letters) > 0:
        print("You have used these letters: ", ' '.join(used_letters))
        word_list = [
            letter if letter in used_letters else '-' for letter in word]
        print('Current word: ', ' '.join(word_list))

        user_letter = input('Guess a letter: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)

        elif user_letter in used_letters:
            print("That letter has been used. Try again!!")

        else:
            print("Invalid characger. Please try again!")
