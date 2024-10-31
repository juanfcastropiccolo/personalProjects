from seasons import convert_to_minutes
import pytest

def test_two_years():
    assert convert_to_minutes("2022-10-11") == "One million, fifty-two thousand, six hundred forty minutes"

def test_america():
    assert convert_to_minutes("1492-10-12") == "Two hundred seventy-nine million, eight hundred three thousand, five hundred twenty minutes"

def test_invalid_date():
    with pytest.raises(SystemExit):
        convert_to_minutes("January 1, 1999")

