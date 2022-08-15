"""Count words in file."""

import sys

# put your code here.
def count_words(text_file):
    word_counts = {}
    file_to_parse = open(text_file)
    for line in file_to_parse:
        line = line.strip()
        words_in_line = line.split(" ")
        for word in words_in_line:
            word = word.casefold()
            word = word.strip('.')
            word = word.strip(',')
            word = word.strip('?')
            word_counts[word] = word_counts.get(word,0) +1
    for key,value in word_counts.items():
        print(f"{key}: {value}")


count_words(text_file=sys.argv[1])

