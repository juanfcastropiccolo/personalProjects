import inflect
p = inflect.engine()

def main():

    names = []

    while True:
        try:
            name = input("Name: ")
            names.append(name)

        except EOFError:
            print()
            break

    new_list = p.join(names)
    print("Adieu, adieu, to " + new_list)

main()

