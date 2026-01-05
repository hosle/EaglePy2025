# https://leetcode.com/problems/insert-interval/
# You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi]
# represent the start and the end of the ith interval and intervals is sorted in ascending order by starti.
# You are also given an interval newInterval = [start, end] that represents the start and end of another interval.
#
# Insert newInterval into intervals such that intervals is still sorted in ascending order by starti
# and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).
#
# Return intervals after the insertion.
#
# Note that you don't need to modify intervals in-place. You can make a new array and return it.
#
#
#
# Example 1:
#
# Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
# Output: [[1,5],[6,9]]
# Example 2:
#
# Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
# Output: [[1,2],[3,10],[12,16]]
# Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
#
#
# Constraints:
#
# 0 <= intervals.length <= 104
# intervals[i].length == 2
# 0 <= starti <= endi <= 105
# intervals is sorted by starti in ascending order.
# newInterval.length == 2
# 0 <= start <= end <= 105
#
# start time :14:40
# end time : 15:37
from typing import List


def test_case1():
    intervals = [[1, 3], [6, 9]]
    new_interval = [2, 5]
    assert solution(intervals, new_interval) == [[1, 5], [6, 9]]


def test_case2():
    intervals = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]
    new_interval = [4, 8]
    assert solution(intervals, new_interval) == [[1, 2], [3, 10], [12, 16]]

def test_case3():
    intervals = list(list())
    new_interval = [4, 8]
    assert solution(intervals, new_interval) == [[4,8]]

def test_case4():
    intervals = [[1,5]]
    new_interval = [2, 7]
    assert solution(intervals, new_interval) == [[1, 7]]

def test_case5():
    intervals = [[1,5]]
    new_interval = [1, 7]
    assert solution(intervals, new_interval) == [[1, 7]]


def solution(intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # bisert new interval and get i

        if len(intervals) == 0:
            return [newInterval]

        left = 0

        right = len(intervals) - 1

        while left <= right:
            mid = (left + right) // 2

            if intervals[mid][0] < newInterval[0]:
                left = mid + 1
            else:
                right = mid - 1

        start_i = left
        print(start_i)
        # merge from i till len(n) - 1
        inter_result = intervals[:start_i] + [newInterval] + intervals[start_i:]
        result = []
        print(inter_result)

        next_interval = inter_result[0]
        for i in range(1, len(inter_result)):
            if next_interval[1] >= inter_result[i][0]:
                next_interval = [next_interval[0], max(inter_result[i][1], next_interval[1])]
                print("merge: ", next_interval)
            else:
                result.append(next_interval)
                next_interval = inter_result[i]

        print(result)
        result.append(next_interval)
        print(result)
        return result

if __name__ == "__main__":
    # test_case1()
    # test_case2()
    # test_case3()
    # test_case4()
    test_case5()