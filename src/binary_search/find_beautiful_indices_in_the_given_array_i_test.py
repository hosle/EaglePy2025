from find_beautiful_indices_in_the_given_array_i import solution
import pytest


@pytest.mark.parametrize("s, a, b, k, expected", [
    ("isawsquirrelnearmysquirrelhouseohmy", "my", "squirrel", 15, [16, 33]),
    ("abcd", "a", "a", 4, [0])
])
def test_case(s, a, b, k, expected):
    assert solution(s, a, b, k) == expected


# def test_case1():
#     s = "isawsquirrelnearmysquirrelhouseohmy"
#     a = "my"
#     b = "squirrel"
#     k = 15
#
#     assert solution(s, a, b, k) == [16, 33]


# def test_case2():
#     s = "abcd"
#     a = "a"
#     b = "a"
#     k = 4
#
#     assert solution(s, a, b, k) == [0]
