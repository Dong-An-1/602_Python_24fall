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

five_letter_word_list = search_words([])


letter_frequencies = {
    'a': 5879, 'e': 5019, 'r': 3640, 'o': 3372, 'i': 3365,
    's': 2954, 'l': 2848, 'n': 2827, 't': 2807, 'u': 2333,
    'c': 1878, 'y': 1870, 'd': 1703, 'm': 1655, 'h': 1639,
    'p': 1508, 'b': 1397, 'g': 1319, 'k': 1121, 'w': 764,
    'f': 755, 'v': 555, 'z': 308, 'j': 251, 'x': 241, 'q': 102
}


def rank_words_by_frequency(word_list, frequency_dict):
    def calculate_score(word):
        return sum(frequency_dict[letter] for letter in word)

    # calculate the score for each word and sort these words by rating
    sorted_words = sorted(word_list, key=lambda word: calculate_score(word), reverse=True)

    # return top5 words
    return sorted_words[:5]



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


def main():
    filtered_words = five_letter_word_list
    grey_letters = []
    green_letters = {}
    yellow_letters = {}

    while True:
        print("\nCurrent number of words in the filtered list:", len(filtered_words))
        print("Top 5 recommended words:", rank_words_by_frequency(filtered_words, letter_frequencies))

        print("\nChoose an action:")
        print("1. Add grey letters")
        print("2. Add yellow letters")
        print("3. Add green letters")
        print("4. View current filtered words")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            grey_input = input("Enter grey letters (separate multiple letters with spaces): ").strip().lower()
            grey_letters.extend(grey_input.split())
            filtered_words = deal_with_grey_letter(filtered_words, grey_letters)
        elif choice == "2":
            yellow_input = input("Enter yellow letters and positions (format: position:letter, separate multiple with commas): ").strip().lower()
            for pair in yellow_input.split(","):
                index, letter = pair.split(":")
                yellow_letters[int(index)] = letter
            filtered_words = deal_with_yellow_letter(filtered_words, yellow_letters)
        elif choice == "3":
            green_input = input("Enter green letters and positions (format: position:letter, separate multiple with commas): ").strip().lower()
            for pair in green_input.split(","):
                index, letter = pair.split(":")
                green_letters[int(index)] = letter
            filtered_words = deal_with_green_letter(filtered_words, green_letters)
        elif choice == "4":
            print("\nCurrent filtered words:")
            print(filtered_words[:10])  # Display only the first 10 words to avoid long outputs
        elif choice == "5":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice, please try again!")

if __name__ == "__main__":
    main()
