def main():
    item = input("Item: ").lower()
    #fda_calories(item)

    item_dictionary = {
        "apple": 130, "avocado": 50, "banana": 110, "cantaloupe": 50, "grapefruit": 60,
        "grapes": 90, "honeydew": 50, "kiwifruit": 90, "lemon": 15, "lime": 20,
        "nectarine": 60, "orange": 80, "peach": 60, "pear": 100, "pineapple": 50, "plums": 70,
        "strawberries": 50, "sweet cherries": 100, "tangerine": 50, "watermelon": 80
        }

    if item in item_dictionary:
        print("Calories:", item_dictionary[item])

"""
def fda_calories(item):
    if item == "apple":
        print("Calories: 130")
    elif item == "avocado":
        print("Calories: 50")
    elif item == "banana":
        print("Calories: 110")
    elif item == "cantaloupe":
        print("Calories: 50")
    elif item == "grapefruit":
        print("Calories: 60")
    elif item == "grapes":
        print("Calories: 90")
    elif item == "honeydew":
        print("Calories: 50")
    elif item == "kiwifruit":
        print("Calories: 90")
    elif item == "lemon":
        print("Calories: 15")
    elif item == "lime":
        print("Calories: 20")
    elif item == "nectarine":
        print("Calories: 60")
    elif item == "orange":
        print("Calories: 80")
    elif item == "peach":
        print("Calories: 60")
    elif item == "pear":
        print("Calories: 100")
    elif item == "pineapple":
        print("Calories: 50")
    elif item == "plums":
        print("Calories: 70")
    elif item == "strawberries":
        print("Calories: 50")
    elif item == "sweet cherries":
        print("Calories: 100")
    elif item == "tangerine":
        print("Calories: 50")
    elif item == "watermelon":
        print("Calories: 80")
    else:
        print("Wrong fruit name. Please insert a correct name.")
"""

main()
