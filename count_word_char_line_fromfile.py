#count_word_char_line_fromfile.py
import os
def word_char_line_count(filename):
    try:
        with open(filename, "r") as f:
            text = f.read()
        words = text.split()
        print("Words:", len(words))
        print("Characters:", len(text))
        print("Lines:", text.count("\n") + 1)
    except FileNotFoundError:
        print("File not found!")
