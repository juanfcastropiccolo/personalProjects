import emoji

def main():
    user_input = input("Input: ")
    emoji_converter(user_input)

def emoji_converter(user_input):
    print("Output: " + emoji.emojize(user_input, language="alias"))

main()
