import random


# Parent Class
class Character:
    def __init__(self, name, character_type, strength, accuracy, intelligence, charisma, socials):
        self._name = name
        self._character_type = character_type
        self._strength = strength
        self._accuracy = accuracy
        self._intelligence = intelligence
        self._charisma = charisma
        self._socials = socials
        self._life_total = 100
        self.potions = 2

    def __str__(self):
        return (f"Name: {self.name}\n"
                f"Class: {self.character_type}\n"
                f"Strength: {self._strength}\n"
                f"Accuracy: {self._accuracy}\n"
                f"Intelligence: {self._intelligence}\n"
                f"Charisma: {self._charisma}\n"
                f"Socials: {self._socials}\n"
                f"Remaining Potions: {self.potions}\n\n"
                f"----------------\n"
                f"Life Total: {self._life_total}\n"
                f"----------------")

    @property # Getter
    def name(self):
        return self._name

    @name.setter # Setter
    def name(self, name):
        if not name:
            raise ValueError("Missing name")
        self._name = name

    @property # Getter
    def character_type(self):
        return self._character_type

    @character_type.setter # Setter
    def character_type(self, character_type):
        if character_type not in [1, 2, 3, 4, 5]:
            raise ValueError("Invalid character")
        self._character_type = character_type

    @property # Getter
    def life_total(self):
        return self._life_total

    @life_total.setter # Setter
    def life_total(self, value):
        if value < 0:
            self._life_total = 0
        else:
            self._life_total = value

    def set_stats(self, stats):
        print("\nSetting your stats...\n")

        self._strength = stats.get("Strength")
        self._accuracy = stats.get("Accuracy")
        self._intelligence = stats.get("Intelligence")
        self._charisma = stats.get("Charisma")
        self._socials = stats.get("Socials")

        print(f"Strength: {self._strength}")
        print(f"Accuracy: {self._accuracy}")
        print(f"Intelligence: {self._intelligence}")
        print(f"Charisma: {self._charisma}")
        print(f"Socials: {self._socials}")

    def healing_potion(self):
        if self.potions:
            self._life_total += 60
            self.potions -= 1
            print(f"{self.name} used a healing potion! Life restored by 60 points.")
        else:
            print("No potions left!")

    def decrease_life(self, amount):
        self._life_total -= amount
        return self._life_total

    # BONUS per skills:
    def use_strength_bonus(self):
        if self._strength > 8:
            self.life_total += 5
            print(f"\nStrength bonus! {self.name} gains 5 extra life points. Current Life Total: {self._life_total}.")

    def intelligence_hint(self):
        if self._intelligence > 8:
            print(f"\n{self.name}'s intelligence provides a hint: Focus on the basics!")

    def charisma_second_chance(self):
        if self._charisma >= 8:
            print(f"\n{self.name}'s charisma gives you a second chance!")
            return True
        return False

    def apply_bonuses(self, correct):
        if correct:
            if self._strength >= 8:
                self.use_strength_bonus()
        elif self._charisma >= 8:
            if self.charisma_second_chance():
                return True
        return False


# Child Classes
class Bandit(Character):
    def __init__(self, name, character_type, strength, accuracy, intelligence, charisma, socials):
        super().__init__(name, character_type, strength, accuracy, intelligence, charisma, socials)
        self.skill_one = "Backstab"
        self.skill_two = "Smoke Bomb"

    def get_skills(self):
        print(f'The skills for your character are "{self.skill_one}" and "{self.skill_two}". Use them wisely...')

class Sorcerer(Character):
    def __init__(self, name, character_type, strength, accuracy, intelligence, charisma, socials):
        super().__init__(name, character_type, strength, accuracy, intelligence, charisma, socials)
        self.skill_one = "Fireball"
        self.skill_two = "Arcane Shield"

    def get_skills(self):
        print(f'The skills for your character are "{self.skill_one}" and "{self.skill_two}". Use them wisely...')

class Necromancer(Character):
    def __init__(self, name, character_type, strength, accuracy, intelligence, charisma, socials):
        super().__init__(name, character_type, strength, accuracy, intelligence, charisma, socials)
        self.skill_one = "Raise Dead"
        self.skill_two = "Life Drain"

    def get_skills(self):
        print(f'The skills for your character are "{self.skill_one}" and "{self.skill_two}". Use them wisely...')

class Druid(Character):
    def __init__(self, name, character_type, strength, accuracy, intelligence, charisma, socials):
        super().__init__(name, character_type, strength, accuracy, intelligence, charisma, socials)
        self.skill_one = "Shapeshift"
        self.skill_two = "Nature's Wrath"

    def get_skills(self):
        print(f'The skills for your character are "{self.skill_one}" and "{self.skill_two}". Use them wisely...')

class Paladin(Character):
    def __init__(self, name, character_type, strength, accuracy, intelligence, charisma, socials):
        super().__init__(name, character_type, strength, accuracy, intelligence, charisma, socials)
        self.skill_one = "Divine Smite"
        self.skill_two = "Holy Shield"

    def get_skills(self):
        print(f'The skills for your character are "{self.skill_one}" and "{self.skill_two}". Use them wisely...')



#################################################################################################
######################################### MAIN METHOD ###########################################
#################################################################################################

def main():
    print("\n✨Welcome to Valhalla!✨ The adventure is about to start!")
    print("Please, pick your Character class to begin.")

    new_character = get_character()
    new_character.get_skills()

    input("\nNow you must roll the dice of destiny... Good luck! HA HA HA \nHit ENTER to continue.")

    while True:
        try:
            stats = get_stats()
            print("Here are your rolled stats:\n")
            for skill, value in stats.items():
                print(f"{skill}: {value}")
            print()

            choice = input("Do you want to keep these stats? Press Enter to keep or type 'r' to reroll: ").lower()

            if choice == '':
                new_character.set_stats(stats)
                break
            else:
                print("Rolling the dice again...")
                continue
        except EOFError:
            break

    print("\nAwesome! These are your new attributes! ✅\n")
    print(new_character)

    input("\nReady for your first adventure...? -Hit ENTER to continue-\n")
    input("In this game, you'll be requested to answer TEN math problems in order to win.\nA correct answer let's you pass. A wrong answer takes 30 points of your Life Total\nBeware of the dark! 🦇🗝️\n\n-Hit ENTER once again-\n")

    # THE GAME STARTS...

    level = get_level()
    total_problems = 10
    correct_answers = 0

    if new_character._intelligence >= 8:
        new_character.intelligence_hint()

    for _ in range(total_problems):

        survived = game_round(new_character, level)

        if survived:
            correct_answers += 1
        if new_character.life_total <= 0:
            break

    if new_character.life_total > 0:
        print(f"\nCongratulations!✨ You survived with a score of {correct_answers} correct answers.\n")

#################################################################################################
####################################### END MAIN METHOD #########################################
#################################################################################################


# Intro functions:
def get_character():
    while True:
        try:
            character_type = int(input("\n1- Bandit\n2- Sorcerer\n3- Necromancer\n4- Druid\n5- Paladin\n\nInsert a number: "))

            if character_type not in [1, 2, 3, 4, 5]:
                print("Please choose a valid option.")
                continue

            name = get_name()

            if character_type == 1:
                print(f"\nGreetings ✨{name}✨, you choosed to be in the side of robbery and mistreat! 🥷 🌙")
                return Bandit(name, "Bandit", 0, 0, 0, 0, 0)
            elif character_type == 2:
                print(f"\nGreetings ✨{name}✨, you choosed the path of fire and ice, lightnings and bolts! ✨ 🧙")
                return Sorcerer(name, "Sorcerer", 0, 0, 0, 0, 0)
            elif character_type == 3:
                print(f"\nGreetings ✨{name}✨, you choosed to seek the undead and the dark lord will guide you! 🧟 👻")
                return Necromancer(name, "Necromancer", 0, 0, 0, 0, 0)
            elif character_type == 4:
                print(f"\nGreetings ✨{name}✨, you choosed to embrace mother nature and all living creatures! 🌲 🐺")
                return Druid(name, "Druid", 0, 0, 0, 0, 0)
            elif character_type == 5:
                print(f"\nGreetings ✨{name}✨, you choosed the path of righteous and fire, protect the king! 🗡 ⛪")
                return Paladin(name, "Paladin", 0, 0, 0, 0, 0)

        except ValueError:
            print("Please enter a valid number for the character type.")

def get_name():
    name = input("What is your name, you brave adventurer...? ")
    return name

def get_stats():
    skill_types = ["Strength", "Accuracy", "Intelligence", "Charisma", "Socials"]
    new_stats = roll_dice()
    skill_results = dict(zip(skill_types, new_stats))
    return skill_results

def roll_dice():
    results = []
    print("\nThe dice of destiny is spinning through the air... 🎲🥁")
    for _ in range(0, 5):
        results.append(random.randint(0, 10))
    return results

# Game functions:
def get_level():
    while True:
        try:
            level = int(input("Choose a Difficulty Level:\n\n1- Easy\n2- Medium\n3- Hard\n\nInsert a number: "))
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


    problem_type = random.choice(['+', '-', '*'])
    problem = f"{x} {problem_type} {y}"
    correct_answer = eval(problem)

    try:
        user_answer = int(input(f"\nSolve this problem: {problem} = "))
        if user_answer == correct_answer:
            print("Correct!")
            return True
        else:
            print(f"Wrong! The correct answer was {correct_answer}.")
            return False
    except ValueError:
        print(f"Invalid input! The correct answer was {correct_answer}.")
        return False

def game_round(character, level):

    if character.life_total <= 20 and character.potions > 0:
        use_potion = input("\nYour Life Total is low! Do you want to use a potion to heal 20 points? (y/n) ").lower()
        if use_potion == "y":
            character.healing_potion()
            print(f"\nNew Life Total: {character.life_total}")

    correct = math_problem_generator(level)

    if correct:
        print(f"{character.name} survived this round!")
        character.apply_bonuses(correct=True)
        return True
    else:
        if character.apply_bonuses(correct=False):
            correct = math_problem_generator(level)
            if correct:
                print(f"{character.name} survived the second chance!")
                character.apply_bonuses(correct=True)
                return True
            else:
                print("Second chance failed!")

        character.decrease_life(30)
        print(f"{character.name}'s current Life Total: {character.life_total} ")

        if character.life_total <= 0:
            print("\nYou have been defeated... Game Over! 👻")
            return False
    return False



if __name__ == "__main__":
    main()
