def main():

    groceries = []

    while True:
        try:
            grocery = input().upper()
            groceries.append(grocery)

        except (EOFError):
            lista_nueva = sorted(set(groceries))
            for i in lista_nueva:
                print(groceries.count(i), i)
            break
        except ValueError:
            pass

main()
