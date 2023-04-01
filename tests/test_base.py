import pytest
from pytest import fixture

import osgood
from osgood.base import ozip, timeit

DEFAULT_LIST = [1, 2, 3, 4]


@pytest.mark.parametrize(
    "passed_int, expected",
    [
        (1, [(1,), (2,), (3,), (4,)]),
        (2, [(1, 2), (3, 4)]),
        (3, [(1, 2, 3)]),
        (4, [(1, 2, 3, 4)]),
        (5, []),
    ],
)
def test_ozip_no_padding(passed_int, expected):
    default_list_value = DEFAULT_LIST
    assert ozip(default_list_value, passed_int) == expected


PAD_BOOL = True


@pytest.mark.parametrize(
    "passed_int, expected",
    [
        (1, [(1,), (2,), (3,), (4,), (None,)]),
        (2, [(1, 2), (3, 4), (None, None)]),
        (3, [(1, 2, 3), (4, None, None)]),
        (4, [(1, 2, 3, 4), (None, None, None, None)]),
        (5, [(1, 2, 3, 4, None)]),
    ],
)
def test_ozip_padding(passed_int, expected):
    default_list_value = DEFAULT_LIST
    default_pad_bool = PAD_BOOL
    assert ozip(default_list_value, passed_int, default_pad_bool) == expected


def simple_loop():
    for i in range(100):
        i += 1


def test_timeit():
    timeit(simple_loop)
