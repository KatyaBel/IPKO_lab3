import pytest

from my_lib import fibonacci


def test1():
    my_list = [1, 1, 2]
    assert fibonacci(3) == my_list


def test2():
    my_list = [1, 1, 2, 3, 5, 8]
    assert fibonacci(6) == my_list


def test3():
    with pytest.raises(TypeError):
        my_list = [1]
        assert fibonacci(5.2) == my_list