from longest_repeating_character_replacement import solution
import pytest


@pytest.mark.parametrize("s, k, expected", [
    ("ABAB", 2, 4),
    ("AABABBA", 1, 4),
    ("AAAAAAA", 1, 7),
    ("ABBAACA", 2, 5)
])
def test_case(s, k, expected):
    assert solution(s, k) == expected


# def test_case1():
#     result = solution("ABAB",2)
#     print(result)
#     assert result == 4


# def test_case2():
#     result = solution("AABABBA", 1)
#     print(result)
#     assert result == 4


# def test_case3():
#     result = solution("AAAAAAA", 1)
#     print(result)
#     assert result == 7


# def test_case4():
#     result = solution("ABBAACA", 2)
#     print(result)
#     assert result == 5
