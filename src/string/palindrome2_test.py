from palindrome2 import solution
import pytest


@pytest.mark.parametrize("input_str, expected", [
    ("bcba", "abcba"),
    ("a", "a"),
    ("bbac", "cabbac"),
    ("abcba", "abcba")
])
def test_case(input_str, expected):
    assert solution(input_str) == expected


# def test_case1():
#     assert "abcba" == solution("bcba")

# def test_case2():
#     assert "a" == solution("a")

# def test_case3():
#     assert "cabbac" == solution("bbac")

# def test_case4():
#     assert "abcba" == solution("abcba")
