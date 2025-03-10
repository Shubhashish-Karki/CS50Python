from twttr import shorten


def test_lowercase():
    assert shorten("your name is") == "yr nm s"


def test_uppercase():
    assert shorten("YOUR NAME IS") == "YR NM S"


def test_numbers():
    assert shorten("1234") == "1234"


def test_punctuations():
    assert shorten("ae,.") == ",."
