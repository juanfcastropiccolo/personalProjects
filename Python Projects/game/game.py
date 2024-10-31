import random
import sys

def main():
    while True:
        try:
            user_level = input("Level: ")

            if user_level.isdigit():
                num_user_level = int(user_level)
                random_number = random.randint(1, num_user_level)
                user_guess = int(input("Guess: "))
                if user_guess < random_number:
                    print("Too small!")
                elif user_guess > random_number:
                    print("Too large!")
                else:
                    print("Just right!")
                    sys.exit()


        except (ValueError, KeyError):
            print("Input valid number")

main()
