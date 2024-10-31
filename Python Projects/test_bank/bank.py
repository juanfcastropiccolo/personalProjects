def main():
    greeting = input("Greeting: ")
    resultado = value(greeting)
    print(resultado)

def value(greeting):
    new_greeting = greeting.lower()
    if new_greeting.startswith("hello"):
        return 0
    elif new_greeting.startswith("h"):
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()
