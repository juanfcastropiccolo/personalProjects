def main():
    word = input("Please, enter a name in camelCase: ")
    snake_case_word = snake_converter(word)
    print(snake_case_word)

def snake_converter(word):
    result = ""
    for letter in word:
        if letter.isupper():
            result += "_" + letter.lower()
        else:
            result += letter
    return result

main()

