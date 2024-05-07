import pytest

from my_lib import calculator


def test1():
    assert calculator(2, 3, '*') == 6


def test2():
    assert calculator(16.4, 4, '/') == 4.1


def test3():
    with pytest.raises(SyntaxError):
        calculator(20, 7, 's')


def test4():
    with pytest.raises(ZeroDivisionError):
        assert calculator(10, 0, '/') == float('inf')