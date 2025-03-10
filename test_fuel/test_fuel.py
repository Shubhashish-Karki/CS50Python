from fuel import convert, gauge
import pytest

#testing for correct input format
def test_correct():
    assert convert('1/5') == 20 and gauge(20) == '20%'
    assert convert('1/100') == 1 and gauge(1) == 'E'
    assert convert('99/100') == 99 and gauge(99) == 'F'

#testing for division by zero
def test_zero_error():
    with pytest.raises(ZeroDivisionError):
        convert('1/0')

#testing for value error
def test_value():
    with pytest.raises(ValueError):
        convert('a/b')