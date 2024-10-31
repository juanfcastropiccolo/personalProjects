def main():
    fraction = input("Fraction: ")
    try:
        percentage = convert(fraction)
        print(gauge(percentage))
    except ZeroDivisionError:
        raise ZeroDivisionError
    except ValueError:
        raise ValueError


def convert(fraction):

    if "/" not in fraction:
        raise ValueError

    new_prompt = fraction.split("/")

    try:
        a = int(new_prompt[0])
        b = int(new_prompt[1])

        if b == 0:
            raise ZeroDivisionError
        if a > b:
            raise ValueError

        return round(a / b * 100)

    except ValueError:
        raise ValueError


def gauge(percentage):
        if percentage <= 1:
            return "E"
        elif percentage >= 99:
            return "F"
        else:
            return f"{percentage}%"


if __name__ == "__main__":
    main()

