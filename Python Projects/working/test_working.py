import pytest
from working import convert

def test_invalid_input():
    with pytest.raises(ValueError):
        convert("09:00 AM to 11:60 AM")


def test_nine_to_five():
    with pytest.raises(ValueError):
        convert("9 to 5")


def test_militar_hour():
    with pytest.raises(ValueError):
        convert("0000 to 1200")


def test_no_period():
    with pytest.raises(ValueError):
        convert("9 to 22")


def test_no_to():
    with pytest.raises(ValueError):
        convert("9 - 22")

def test_no_to_no_spaces():
    with pytest.raises(ValueError):
        convert("9AM - 22PM")

def test_three_times():
    with pytest.raises(ValueError):
        convert("9 to 22 to 23")


def test_off_by_one():
    assert convert("9 PM to 12 AM") == "21:00 to 00:00"
    assert convert("8 PM to 12 AM") == "20:00 to 00:00"
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("10 PM to 8 AM") == "22:00 to 08:00"
    assert convert("10:00 PM to 8:00 AM") == "22:00 to 08:00"
    assert convert("12 AM to 12 PM") == "00:00 to 12:00"
    assert convert("12:00 AM to 12:00 PM") == "00:00 to 12:00"


def test_off_by_five():
    assert convert("9:05 PM to 12:05 AM") == "21:05 to 00:05"
