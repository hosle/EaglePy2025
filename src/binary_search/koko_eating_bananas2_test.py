from koko_eating_bananas2 import solution
import pytest


@pytest.mark.parametrize("piles, h, expected", [
    ([3, 6, 7, 11], 8, 4),
    ([30,11,23,4,20], 5, 30),
    ([30,11,23,4,20], 6, 23),
    ([312884470], 312884469, 2),
    ([2,2], 2, 2)
])
def test_case(piles, h, expected):
    assert solution(piles, h) == expected


# def test_case1():
#     piles = [3, 6, 7, 11]
#     h = 8
#
#     assert solution(piles, h) == 4


# def test_case2():
#     piles = [30,11,23,4,20]
#     h = 5
#
#     assert solution(piles, h) == 30


# def test_case3():
#     piles = [30,11,23,4,20]
#     h = 6
#
#     assert solution(piles, h) == 23

# def test_case4():
#     piles = [312884470]
#     h = 312884469
#
#     assert solution(piles, h) == 2

# def test_case5():
#     piles = [2,2]
#     h = 2
#     assert solution(piles, h) == 2
