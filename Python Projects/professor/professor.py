import random


def main():

    level = get_level()
    amount = 10
    correct = 0

    for _ in range(amount):
        if math_problem_generator(level):
            correct += 1

    print(f"Score: {correct}")

def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level in [1, 2, 3]:
                return level
        except ValueError:
            print("Incorrect Input!")

def get_ans():
    while True:
        try:
            user_answer = int(input())
            return user_answer
        except ValueError:
            print("Incorrect Input!")

def math_problem_generator(level):
    if level == 1:
        x = random.randint(0, 9)
        y = random.randint(0, 9)
    elif level == 2:
        x = random.randint(10, 99)
        y = random.randint(10, 99)
    elif level == 3:
        x = random.randint(100, 999)
        y = random.randint(100, 999)
    else:
        raise ValueError


    for attempts in range(3):
        print(f"{x} + {y} = ", end="")
        z = get_ans()

        if (z == x + y):
            return True
        else:
            print("EEE")

    print(f"{x} + {y} = {x + y}")
    return False



if __name__ == "__main__":
    main()
