from plates import is_valid

def test_min():
    assert is_valid("a") == False
    assert is_valid("1") == False

def test_max():
    assert is_valid("abcdefghi") == False
    assert is_valid("abcdef123") == False

def test_letter():
    assert is_valid("abcd23") == True
    assert is_valid("ab23") == True
    assert is_valid("1234") == False

def test_punctuation():
    assert is_valid("abc_2") == False
    assert is_valid(" bcd") == False
    assert is_valid("a.cbd2") == False

def test_zero():
    assert is_valid("ab012") == False

def test_notzero():
    assert is_valid("ab120") == True

def test_number():
    assert is_valid("ab1cd") == False
    assert is_valid("ab123") == True