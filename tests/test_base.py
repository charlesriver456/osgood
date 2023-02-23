import osgood
from osgood.base import ozip
import pytest


@pytest.mark.parametrize(
    "test_list, passed_int, expected",
    [([1, 2, 3, 4], 4, [(1, 2, 3, 4)]), ([1, 2, 3], 4, []), ([1, 2, 3], 2, [(1, 2)])],
)
def test_ozip_1(test_list, passed_int, expected):
    assert ozip(test_list, passed_int) == expected
