from numb3rs import validate


def test_first():
    assert validate("1.2.3.4") == True
    assert validate("256.2.3.4") == False


def test_second():
    assert validate("1.2.3.4") == True
    assert validate("1.256.3.4") == False


def test_third():
    assert validate("1.2.3.4") == True
    assert validate("2.2.256.4") == False


def test_fourth():
    assert validate("1.2.3.4") == True
    assert validate("2.2.3.256") == False


def test_strings():
    assert validate("cat 1.3.4.5") == False
    assert validate("1.cat.3.4") == False
