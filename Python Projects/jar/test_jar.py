from jar import Jar
import pytest

def test_deposit():
    jar = Jar()
    jar.deposit(5)
    assert jar.size == 5

def test_withdraw():
    jar = Jar()
    jar.deposit(5)
    jar.withdraw(2)
    assert jar.size == 3

def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"

def test_maxed_capacity():
    jar = Jar()
    with pytest.raises(ValueError):
        jar.deposit(13)

