def convert(text: str):
    return text.replace(":)", "🙂").replace(":(", "🙁")


def main():
    new_text = input("Ingrese su texto: ")
    print(convert(new_text))

main()
