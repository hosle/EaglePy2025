from minimum_operations_to_reduce_an_integer_to_0 import solution
import pytest


@pytest.mark.parametrize("n, expected", [
    (39, 3),
    (54, 3)
])
def test_case(n, expected):
    assert solution(n) == expected


# def test_case1():
#     n = 39
#     assert solution(n) == 3


# def test_case2():
#     n = 54
#     assert solution(n) == 3
