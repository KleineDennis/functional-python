import pytest

def func(x):
    return x + 1


def test_answer():
    assert func(3) == 4 #5


def test_raises_exception():
    with pytest.raises(ZeroDivisionError):
        1 / 0
