import re
import sys


def main():
    print(count(input("Text: ")))


def count(text_input):
    pattern = r"\bum\b"

    matches = re.findall(pattern, text_input, flags=re.IGNORECASE)

    return len(matches)



if __name__ == "__main__":
    main()
