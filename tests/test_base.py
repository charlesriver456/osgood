import os

import pytest

from osgood.base import ozip, rossum_rip, timeit, gcd

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

def test_rossum_rip_py_file() -> None:
    test_file_name = os.path.dirname(os.path.realpath(__file__)) + "/test_file.py"
    with open(test_file_name, "w") as test_file:
        test_file.write(
            """def foo():
    (example_var := 1)
    return 1""")
    rossum_rip(test_file_name)
    with open(test_file_name) as edited_file:
        edited_file_text = edited_file.read()
    correct_text = """def foo():
    (example_var = 1)
# WALRUS REMOVED ABOVE, DOUBLE CHECK
    return 1"""
    os.remove(test_file_name)
    assert edited_file_text.replace(" ", "") == correct_text.replace(" ", "")

def test_rossum_rip_string() -> None:
    example_string = "I am an ardent walrus user. Here is an example: (example_var := 1)."
    correct_text = rossum_rip(example_string, file_flag=False)
    expected_correct_text = "I am an ardent walrus user. Here is an example: (example_var = 1)."
    assert correct_text == expected_correct_text

def test_gcd() -> None:
    num1 = 100
    num2 = 50
    expected_gcd = 50
    ans = gcd(num1, num2)
    assert expected_gcd == ans

def test_gcd_edge() -> None:
    num1 = 0
    num2 = 50
    expected_gcd = 50
    ans = gcd(num1, num2)
    assert expected_gcd == ans

def test_gcd_double_edge() -> None:
    num1 = 0
    num2 = 0
    expected_gcd = 0
    ans = gcd(num1, num2)
    assert expected_gcd == ans