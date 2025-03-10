from um import count
import pytest


def test_no_um():
    assert count("hello how are you") == 0


def test_um_in_words():
    assert count("bacterium") == 0


def test_um():
    assert count("um") == 1
    assert count("um yummy um..") == 2

def test_case():
    assert count("UM uM Um") == 3