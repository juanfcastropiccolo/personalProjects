def main():
    text = input("Input: ")
    vowel_remover(text)

def vowel_remover(text):
    new_word = ""
    for letter in text:
        if letter in ("a", "e", "i", "o", "u", "A", "E", "I", "O", "U"):
            new_word += ""
        else:
            new_word += letter
    print(new_word)


main()
