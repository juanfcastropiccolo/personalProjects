from plates import is_valid

def test_starts_with_two():
    assert is_valid("NRVOUS") == True

def test_max_letters_six():
    assert is_valid("NRVOUSSS") == False

def test_numbs_in_middle():
    assert is_valid("AAA222") == True

def test_punctuation_check():
    assert is_valid("PI3.14") == False

def test_min_valid():
    assert is_valid("50") == False

def test_number_at_the_end():
    assert is_valid("ECTO88") == True

def test_zero_at_beginning():
    assert is_valid("AAA001") == False

def test_number_placement():
    assert is_valid("CS50P2") == False
