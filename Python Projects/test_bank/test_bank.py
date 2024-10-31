from bank import value

def test_first_if():
    assert value("hello") == 0

def test_second_if():
    assert value("hey") == 20

def test_else():
    assert value("aloha") == 100

def test_case():
    assert value("Hello") == 0
