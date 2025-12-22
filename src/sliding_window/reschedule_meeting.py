# https://leetcode.com/problems/reschedule-meetings-for-maximum-free-time-i/description/
# You are given an integer eventTime denoting the duration of an event, where the event occurs from time t = 0 to time t = eventTime.
#
# You are also given two integer arrays startTime and endTime, each of length n. These represent the start and end time of n non-overlapping meetings, where the ith meeting occurs during the time [startTime[i], endTime[i]].
#
# You can reschedule at most k meetings by moving their start time while maintaining the same duration, to maximize the longest continuous period of free time during the event.
#
# The relative order of all the meetings should stay the same and they should remain non-overlapping.
#
# Return the maximum amount of free time possible after rearranging the meetings.
#
# Note that the meetings can not be rescheduled to a time outside the event.
from collections import deque
from typing import List

from huggingface_hub.cli.system import env


# Constraints:
#
# 1 <= eventTime <= 109
# n == startTime.length == endTime.length
# 2 <= n <= 105
# 1 <= k <= n
# 0 <= startTime[i] < endTime[i] <= eventTime
# endTime[i] <= startTime[i + 1] where i lies in the range [0, n - 2].

# start time 15:03
# end time

#         n = len(startTime)
#         gaps = [0] * (n + 1)
#
#         # Compute gaps
#         gaps[0] = startTime[0]
#         gaps[n] = eventTime - endTime[-1]
#         for i in range(1, n):
#             gaps[i] = startTime[i] - endTime[i - 1]
#
#         # Sliding window of size k + 1
#         window = sum(gaps[:k + 1])
#         ans = window
#         for i in range(k + 1, n + 1):
#             window += gaps[i] - gaps[i - (k + 1)]
#             ans = max(ans, window)
#
#         return ans

def solution(eventTime: int, k: int, startTime: List[int], endTime: List[int]) -> int:
    # find all the free duration

    free_interval = list()

    if startTime[0] > 0:
        free_interval.append(startTime[0])

    for i in range(1, len(startTime)):
        free_interval.append(startTime[i] - endTime[i-1])

    if endTime[-1] < eventTime:
        free_interval.append(eventTime - endTime[-1])

    print("free_interval =", free_interval)

    result = 0

    i = 0
    while i < len(free_interval) and i < k + 1:
        result += free_interval[i]
        i += 0

    print("init result =", result)

    j = k+1
    window = result
    while j < len(free_interval):
        window = window + free_interval[j] - free_interval[j - k - 1]
        result = max(window, result)
        j += 1

    return result


def test_case1():
    result = solution(5, 1, [1, 3], [2, 5])
    print("test 1 = ", result)
    assert result == 2

def test_case2():
    result = solution(10, 1, [0, 2, 9], [1, 4, 10])
    print("test 2 = ", result)
    assert result == 6

def test_case3():
    result = solution(5, 2, [0, 1, 2, 3, 4], [1, 2, 3, 4, 5])
    print("test 3 = ", result)
    assert result == 0

def test_case4():
    result = solution(21, 1, [7, 10, 16], [10, 14, 18])
    print("test 4 = ", result)
    assert result == 7

def test_case5():
    result = solution(30, 2, [1, 15, 17], [14,17,29])
    print("test 5 = ", result)
    assert result == 2

def test_case6():
    result = solution(99, 1, [7, 21, 25], [13, 25, 78])
    print("test 6 = ", result)
    assert result == 21


if __name__ == "__main__":
    # test_case1()
    # test_case2()
    # test_case3()
    test_case4()
    test_case5()
    test_case6()