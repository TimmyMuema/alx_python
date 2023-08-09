#!/usr/bin/python3
def get_first_three_letters(word):
    return word[:3]

def get_last_two_letters(word):
    return word[-2:]

def get_middle_word(word):
    return word[1:-1]

word = "Holberton"

word_first_3 = get_first_three_letters(word)
word_last_2 = get_last_two_letters(word)
middle_word = get_middle_word(word)

print("First 3 letters:", word_first_3)
print("Last 2 letters:", word_last_2)
print("Middle word:", middle_word)
