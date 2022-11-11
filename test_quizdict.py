import pytest
from quizdict import get_percent


def test_get_percent_low():
    assert get_percent(1, 200) == 0.5

def test_get_percent_high():
    assert get_percent(1000000000, 2000000000) == 50

def test_get_percent_reverse():
    assert get_percent(2, 1) == 200

