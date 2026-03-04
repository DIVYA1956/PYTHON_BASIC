# vowel_counter.py

def count_vowels(text):
    vowels = "aeiouAEIOU"
    count = 0
    for ch in text:
        if ch in vowels:
            count += 1
    return count

sentence = input("Enter a sentence: ")
vowel_count = count_vowels(sentence)
print(f"Total number of vowels: {vowel_count}")