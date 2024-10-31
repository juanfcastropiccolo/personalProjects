from numb3rs import validate

def test_out_of_limits():
    assert validate("1000.123.123.123") == False
    assert validate("256.123.123.123") == False
    assert validate("123.256.123.123") == False

def test_not_numbers():
    assert validate("cat") == False

def test_inside_limits():
    assert validate("255.255.255.255") == True

def test_by_group():
    assert validate("1.2.3.1000") == False

def test_too_many_groups():
    assert validate("123.123.123.123.123") == False

