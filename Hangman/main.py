
import random
import string

from words import words

print(words)

def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or '' in word
        word = random.choice(words)
    return word

def hangman():
    word = get_valid_word(words)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letter = set()

    used_letter =