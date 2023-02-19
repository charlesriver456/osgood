import osgood
from osgood.base import ozip
import typing


def test_ozip_1():
    example_list = [1, 2, 3, 4]
    example_group = 4
    response = ozip(example_list, example_group)
    assert response == [(1, 2, 3, 4)]


def test_ozip_2():
    example_list = [1, 2, 3]
    example_group = 4
    response = ozip(example_list, example_group)
    assert response == []


def test_ozip_3():
    example_list = [1, 2, 3]
    example_group = 2
    response = ozip(example_list, example_group)
    assert response == [(1, 2)]
