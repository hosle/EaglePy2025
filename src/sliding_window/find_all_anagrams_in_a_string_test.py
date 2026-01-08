from find_all_anagrams_in_a_string import solution
import pytest


@pytest.mark.parametrize("s, p, expected", [
    ("cbaebabacd", "abc", [0,6]),
    ("abab", "ab", [0,1,2]),
    ("aaabb", "bb", [3])
])
def test_case(s, p, expected):
    assert solution(s, p) == expected


# def test_case1():
#     result = solution("cbaebabacd", "abc")
#     print(result)
#     assert result == [0,6]


# def test_case2():
#     result = solution("abab", "ab")
#     print(result)
#     assert result == [0,1,2]


# def test_case3():
#     result = solution("aaabb", "bb")
#     print(result)
#     assert result == [3]
