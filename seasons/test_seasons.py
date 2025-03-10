from seasons import convert
import pytest


def test_format():
    with pytest.raises(SystemExit):
        convert("January 1, 1999")


def test():
    assert (
        convert("2023-02-21")
        == "Five hundred twenty-five thousand, six hundred minutes"
    )
