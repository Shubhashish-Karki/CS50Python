from working import convert
import pytest

def test_hour():
    with pytest.raises(ValueError):
        convert("13 PM to 17 PM")


def test_min():
    with pytest.raises(ValueError):
        convert("9:60 AM to 9:60 PM")


def test_format():
    with pytest.raises(ValueError):
        convert("9 AM - 9 PM")


def test():
   assert convert("9 AM to 5 PM") == "09:00 to 17:00"
   assert convert("10:30 PM to 8:50 AM") == "22:30 to 08:50"
