def main():
    while True:
        prompt = input("Fraction: ")
        if formatter(prompt):
            break

def formatter(prompt):
    new_prompt = prompt.split("/")

    try:
        a = int(new_prompt[0])
        b = int(new_prompt[1])
        if a > b:
            return False
        elif a == b and a != 0:
            print("F")
            return True
        elif a == 99 and b == 100:
            print("F")
            return True
        elif a != b and a == 0:
            print("E")
            return True
        elif a <= 1 and b == 100:
            print("E")
            return True
        else:
            print(str(round(a / b * 100)) + "%")
            return True


    except (ValueError, ZeroDivisionError):
        return False

main()
