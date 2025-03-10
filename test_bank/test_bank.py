from bank import value

def test_100():
    assert value("asdfg") == 100        #testing for alphabets
    assert value("1234") == 100         #testing for numerals
    assert value("adf.xv12") == 100     #testing for alphanumerals

def test_20():
    assert value("hey") == 20           #testing for lowercase
    assert value("Hey") == 20           #testing for uppercase

def test_0():
    assert value("hello") == 0
    assert value("Hello") == 0
    assert value("Hello, my name is David") == 0    #testing for sentence