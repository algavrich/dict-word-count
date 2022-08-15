"""Count words in file."""

import sys

# put your code here.
def count_words_dict(text_file):
    """takes text_file as argument

    prints statement of how many times each word 
    appears in document
    """
    def tokenize(text_file):
        """

        return list of words from entire file
        """
        words = []
        file = open(text_file)
        for line in file:
            line = line.strip()
            words_in_line = line.split(" ")
            for word in words_in_line:
                word = word.casefold()
                word = word.strip('.')
                word = word.strip(',')
                word = word.strip('?')
                words.append(word)
        return words
    # print(tokenize(text_file))

    def count_words(words):
        """
        Take in a list of strings and return a dictionary of each string and the number of times it appears in the list.
        """
        word_counts = {}
        for word in words:
             word_counts[word] = word_counts.get(word,0) +1

        return word_counts
    # print(count_words(tokenize(text_file)))

    def print_word_counts(word_counts):
        for word, count in word_counts.items():
            print(f"{word} {count}")

    print_word_counts(count_words(tokenize(text_file)))


    # Old code without inner functions
    # word_counts = {}
    # file_to_parse = open(text_file)
    # for line in file_to_parse:
    #     line = line.strip()
    #     words_in_line = line.split(" ")
    #     for word in words_in_line:
    #         word = word.casefold()
    #         word = word.strip('.')
    #         word = word.strip(',')
    #         word = word.strip('?')
    #         word_counts[word] = word_counts.get(word,0) +1
    # for key,value in word_counts.items():
    #     pass
        # print(f"{key} {value}")


count_words_dict(text_file=sys.argv[1])

