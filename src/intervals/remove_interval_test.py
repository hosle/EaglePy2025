from remove_interval import solution
import pytest


@pytest.mark.parametrize("intervals, toBeRemoved, expected", [
    ([[0,2],[3,4],[5,7]], [1,6], [[0,1],[6,7]]),
    ([[0, 5]], [2, 3], [[0,2],[3,5]]),
    ([[-5, -4], [-3, -2], [1, 2], [3, 5], [8, 9]], [-1, 4], [[-5,-4],[-3,-2],[4,5],[8,9]])
])
def test_case(intervals, toBeRemoved, expected):
    assert solution(intervals, toBeRemoved) == expected


# def test_case0():
#     intervals = [[0,2],[3,4],[5,7]]
#     toBeRemoved = [1,6]
#     assert solution(intervals, toBeRemoved) == [[0,1],[6,7]]


# def test_case1():
#     intervals = [[0, 5]]
#     toBeRemoved = [2, 3]
#     assert solution(intervals, toBeRemoved) == [[0,2],[3,5]]


# def test_case2():
#     intervals = [[-5, -4], [-3, -2], [1, 2], [3, 5], [8, 9]]
#     toBeRemoved = [-1, 4]
#     assert solution(intervals, toBeRemoved) == [[-5,-4],[-3,-2],[4,5],[8,9]]
