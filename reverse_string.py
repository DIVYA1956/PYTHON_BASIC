def reverse_string(text):
    return text[::-1]

word = input("Enter a word: ")

result = reverse_string(word)

print("Reversed:", result)