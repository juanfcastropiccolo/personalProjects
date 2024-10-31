from project import roll_dice, get_character, math_problem_generator, game_round
from project import Character, Bandit, Sorcerer, Necromancer, Druid, Paladin
import pytest



def test_bandit_character_initialization():
    new_bandit = Bandit("Juan", "Bandit", 5, 6, 7, 8, 9)
    assert new_bandit.name == "Juan"
    assert new_bandit.character_type == "Bandit"
    assert new_bandit.skill_one == "Backstab"
    assert new_bandit.skill_two == "Smoke Bomb"

def test_sorcerer_character_initialization():
    new_sorcerer = Sorcerer("Juan", "Sorcerer", 5, 6, 7, 8, 9)
    assert new_sorcerer.name == "Juan"
    assert new_sorcerer.character_type == "Sorcerer"
    assert new_sorcerer.skill_one == "Fireball"
    assert new_sorcerer.skill_two == "Arcane Shield"

def test_necromancer_character_initialization():
    new_necromancer = Necromancer("Juan", "Necromancer", 5, 6, 7, 8, 9)
    assert new_necromancer.name == "Juan"
    assert new_necromancer.character_type == "Necromancer"
    assert new_necromancer.skill_one == "Raise Dead"
    assert new_necromancer.skill_two == "Life Drain"

def test_druid_character_initialization():
    new_druid = Druid("Juan", "Druid", 5, 6, 7, 8, 9)
    assert new_druid.name == "Juan"
    assert new_druid.character_type == "Druid"
    assert new_druid.skill_one == "Shapeshift"
    assert new_druid.skill_two == "Nature's Wrath"

def test_paladin_character_initialization():
    new_paladin = Paladin("Juan", "Paladin", 5, 6, 7, 8, 9)
    assert new_paladin.name == "Juan"
    assert new_paladin.character_type == "Paladin"
    assert new_paladin.skill_one == "Divine Smite"
    assert new_paladin.skill_two == "Holy Shield"

def test_name_setter_getter():
    character = Character("Juan", "Bandit", 5, 5, 5, 5, 5)
    character.name = "Juan"
    assert character.name == "Juan"

def test_name_setter_invalid():
    character = Character("John", "Bandit", 5, 5, 5, 5, 5)
    try:
        character.name = ""
    except ValueError as e:
        assert str(e) == "Missing name"

def test_roll_dice():
    result = roll_dice()
    assert len(result) == 5
    for num in result:
        assert 0 <= num <= 10

def test_problems():
    with pytest.raises(ValueError):
        math_problem_generator(4)
        math_problem_generator("Dog")
        math_problem_generator(5)
        math_problem_generator("Cat")
        math_problem_generator("")

def test_charisma_second_chance():
    new_character = Character("Michael", 1, 5, 5, 5, 8, 5)
    assert new_character.charisma_second_chance() == True

def test_no_second_chance():
    new_character = Character("Mike", 1, 5, 5, 5, 7, 5)
    assert new_character.charisma_second_chance() == False

def test_no_more_potions():
    new_character = Character("Miguel", 1, 5, 5, 5, 8, 5)
    new_character.potions = 0
    new_character.life_total = 10
    new_character.healing_potion()
    assert new_character.life_total == 10