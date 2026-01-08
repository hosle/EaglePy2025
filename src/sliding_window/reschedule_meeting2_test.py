from reschedule_meeting2 import solution
import pytest


@pytest.mark.parametrize("eventTime, k, startTime, endTime, expected", [
    (5, 1, [1, 3], [2, 5], 2),
    (10, 1, [0, 2, 9], [1, 4, 10], 6),
    (5, 2, [0, 1, 2, 3, 4], [1, 2, 3, 4, 5], 0),
    (21, 1, [7, 10, 16], [10, 14, 18], 7),
    (30, 2, [1, 15, 17], [14,17,29], 2),
    (99, 1, [7, 21, 25], [13, 25, 78], 21)
])
def test_case(eventTime, k, startTime, endTime, expected):
    assert solution(eventTime, k, startTime, endTime) == expected


# def test_case1():
#     result = solution(5, 1, [1, 3], [2, 5])
#     print("test 1 = ", result)
#     assert result == 2

# def test_case2():
#     result = solution(10, 1, [0, 2, 9], [1, 4, 10])
#     print("test 2 = ", result)
#     assert result == 6

# def test_case3():
#     result = solution(5, 2, [0, 1, 2, 3, 4], [1, 2, 3, 4, 5])
#     print("test 3 = ", result)
#     assert result == 0

# def test_case4():
#     result = solution(21, 1, [7, 10, 16], [10, 14, 18])
#     print("test 4 = ", result)
#     assert result == 7

# def test_case5():
#     result = solution(30, 2, [1, 15, 17], [14,17,29])
#     print("test 5 = ", result)
#     assert result == 2

# def test_case6():
#     result = solution(99, 1, [7, 21, 25], [13, 25, 78])
#     print("test 6 = ", result)
#     assert result == 21
