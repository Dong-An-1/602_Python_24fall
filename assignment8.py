# Copyright 2024 Dong An dong@bu.edu
# Copyright 2024 Shenghan Wu wshwsh@bu.edu
# Copyright 2024 Ziheng Qu heng24@bu.edu

import nltk
from nltk.corpus import words

# Offline methods: NLTK(the method we choose to use) and PyEnchant are suitable for scenarios requiring local processing.
# Online APIs: Datamuse and Wordnik provide richer word databases but require an internet connection.

nltk.download('words')

# Load the word list
word_list = [word.lower() for word in words.words()]

# Filter words based on the number of letters and required letters
def search_words(required_letters):
    return [
        word for word in word_list
        if len(word) == 5 and all(letter in word for letter in required_letters)
    ]

five_letter_word_list = search_words(['c'])

def deal_with_grey_letter(filtered_word_list, grey_letters):
    """
    Filter the word list by excluding words containing any of the grey letters.

    :param filtered_word_list: The current list of words to filter
    :param grey_letters: A list of grey letters that should not appear in the words
    :return: A filtered list of words that do not contain any of the grey letters
    """
    return [
        word for word in filtered_word_list
        if not any(letter in word for letter in grey_letters)
    ]

def deal_with_green_letter(filtered_words, green_letters):
    """
    Filter the word list based on green letters and their positions.

    :param filtered_words: The current list of words to filter
    :param green_letters: Green letters and their corresponding positions, in the format {index: 'letter'}
    :return: A filtered list of words matching the green letters at their specified positions
    """
    return [
        word for word in filtered_words
        if all(word[index] == letter for index, letter in green_letters.items())
    ]

def deal_with_yellow_letter(filtered_words, yellow_letters):
    """
    Filter the word list based on yellow letters and their positions.

    :param filtered_words: The current list of words to filter
    :param yellow_letters: Yellow letters and their corresponding positions, in the format {index: 'letter'}
    :return: A filtered list of words that contain the yellow letters but not at the specified positions
    """
    return [
        word for word in filtered_words
        if all(
            letter in word and word[index] != letter
            for index, letter in yellow_letters.items()
        )
    ]




# testcase

# filtered_words = deal_with_grey_letter(five_letter_word_list,['a','r','e','d'])
# filtered_words = deal_with_yellow_letter(filtered_words,{1:'c'})
# filtered_words = deal_with_green_letter(filtered_words, {})
#
# filtered_words = deal_with_grey_letter(filtered_words,['l','k'])
# filtered_words = deal_with_yellow_letter(filtered_words,{2:'i'})
# filtered_words = deal_with_green_letter(filtered_words, {3:'c'})
#
# filtered_words = deal_with_grey_letter(filtered_words,['b'])
# filtered_words = deal_with_yellow_letter(filtered_words,{})
# filtered_words = deal_with_green_letter(filtered_words, {1:'i',2:'t',3:'c',4:'h'})
# print(filtered_words)

# The answer is “which”.
# In this testcase, the output we got after trying three times is ['fitch', 'hitch', 'mitch', 'nitch', 'pitch', 'sitch', 'witch']
# We can only try the rest words one by one. It may not ensure us to win the game, but can help us increase win rate.
