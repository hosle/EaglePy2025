from insert_interval import solution
import pytest


@pytest.mark.parametrize("intervals, newInterval, expected", [
    ([[1, 3], [6, 9]], [2, 5], [[1, 5], [6, 9]]),
    ([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8], [[1, 2], [3, 10], [12, 16]]),
    ([], [4, 8], [[4,8]]),
    ([[1,5]], [2, 7], [[1, 7]]),
    ([[1,5]], [1, 7], [[1, 7]])
])
def test_case(intervals, newInterval, expected):
    assert solution(intervals, newInterval) == expected


# def test_case1():
#     intervals = [[1, 3], [6, 9]]
#     new_interval = [2, 5]
#     assert solution(intervals, new_interval) == [[1, 5], [6, 9]]


# def test_case2():
#     intervals = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]
#     new_interval = [4, 8]
#     assert solution(intervals, new_interval) == [[1, 2], [3, 10], [12, 16]]

# def test_case3():
#     intervals = list(list())
#     new_interval = [4, 8]
#     assert solution(intervals, new_interval) == [[4,8]]

# def test_case4():
#     intervals = [[1,5]]
#     new_interval = [2, 7]
#     assert solution(intervals, new_interval) == [[1, 7]]

# def test_case5():
#     intervals = [[1,5]]
#     new_interval = [1, 7]
#     assert solution(intervals, new_interval) == [[1, 7]]
