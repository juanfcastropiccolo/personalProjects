def main():
    text = input("Input: ")
    print(shorten(text))

def shorten(word):
    new_word = ""
    for letter in word:
        if letter in ("a", "e", "i", "o", "u", "A", "E", "I", "O", "U"):
            new_word += ""
        else:
            new_word += letter
    return new_word

if __name__ == "__main__":
    main()
