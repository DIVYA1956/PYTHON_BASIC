# vowel_counter.py

def count_vowels(text):
    vowels = "aeiouAEIOU"
    count = 0

    for ch in text:
        if ch in vowels:
            count += 1

    return count


def main():
    sentence = input("Enter a sentence: ")

    if not sentence.strip():
        print("Input cannot be empty.")
        return

    vowel_count = count_vowels(sentence)
    print(f"Total vowels in your sentence: {vowel_count}")


if __name__ == "__main__":
    main()