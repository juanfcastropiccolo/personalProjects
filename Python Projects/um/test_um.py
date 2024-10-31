from um import count
import pytest

def test_yummy():
    assert count("yummy") == 0

def test_comma():
    assert count("hello,um") == 1

def test_question():
    assert count("um?") == 1

def test_thanks():
    assert count("Um, thanks, um...") == 2
