from interval_list_intersections import solution
import pytest


@pytest.mark.parametrize("firstList, secondList, expected", [
    ([[0, 2], [5, 10], [13, 23], [24, 25]], [[1, 5], [8, 12], [15, 24], [25, 26]], [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]),
    ([[1, 3], [5, 9]], [], []),
    ([[1, 3], [5, 9]], [[5, 6]], [[5,6]])
])
def test_case(firstList, secondList, expected):
    assert solution(firstList, secondList) == expected


# def test_case1():
#     firstList = [[0, 2], [5, 10], [13, 23], [24, 25]]
#     secondList = [[1, 5], [8, 12], [15, 24], [25, 26]]
#
#     assert solution(firstList, secondList) == [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]


# def test_case2():
#     firstList = [[1, 3], [5, 9]]
#     secondList = []
#
#     assert solution(firstList, secondList) == []

# def test_case3():
#     firstList = [[1, 3], [5, 9]]
#     secondList = [[5, 6]]
#
#     assert solution(firstList, secondList) == [[5,6]]
