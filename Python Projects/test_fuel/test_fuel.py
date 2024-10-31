from fuel import convert, gauge
import pytest

def test_fuel():
    assert convert("2/4") == 50

def test_incorrect_ints():
    with pytest.raises(ValueError):
        convert("4/2")

def test_gauge():
    assert gauge(99) == "F"

def test_value_error():
    with pytest.raises(ValueError):
        convert("hello")

def test_invalid_format():
    with pytest.raises(ValueError):
        convert("3-3")

def test_gauge_1_percent():
    assert gauge(1) == "E"

def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        convert("4/0")

def test_gauge_percentage():
    assert gauge(50) == "50%"
    assert gauge(75) == "75%"
