# count_word_char_line_fromfile.py

def word_char_line_count(filename):
    try:
        with open(filename, "r") as f:
            text = f.read()

        words = text.split()
        word_count = len(words)
        char_count = len(text)
        line_count = text.count("\n") + 1

        return word_count, char_count, line_count

    except FileNotFoundError:
        print("File not found!")
        return None


def main():
    filename = input("Enter file name: ")

    result = word_char_line_count(filename)

    if result:
        words, chars, lines = result
        print("Words:", words)
        print("Characters:", chars)
        print("Lines:", lines)


if __name__ == "__main__":
    main()