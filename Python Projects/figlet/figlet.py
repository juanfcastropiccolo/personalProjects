import pyfiglet
from pyfiglet import Figlet
figlet = Figlet()
import sys
import random


if sys.argv[1] == "-f" and sys.argv[2] in figlet.getFonts():
    try:
        user_input = input("Input: ")
        figlet.setFont(font=sys.argv[2])
        print(figlet.renderText(user_input))
    except IndexError:
        sys.exit("Invalid usage")
elif sys.argv[1] != "-f":
    sys.exit("Invalid usage")
elif sys.argv[2] not in figlet.getFonts():
    sys.exit("Invalid usage")
else:
    user_input = input("Input: ")
    random_font = random.choice(figlet.getFonts())
    figlet.setFont(font=random_font)
    print(figlet.renderText(user_input))



