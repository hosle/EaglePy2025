# https://leetcode.com/problems/find-right-interval/description/
# You are given an array of intervals, where intervals[i] = [starti, endi] and each starti is unique.
#
# The right interval for an interval i is an interval j such that startj >= endi and startj is minimized.
# Note that i may equal j.
#
# Return an array of right interval indices for each interval i.
# If no right interval exists for interval i, then put -1 at index i.
#
#
#
# Example 1:
#
# Input: intervals = [[1,2]]
# Output: [-1]
# Explanation: There is only one interval in the collection, so it outputs -1.
# Example 2:
#
# Input: intervals = [[3,4],[2,3],[1,2]]
# Output: [-1,0,1]
# Explanation: There is no right interval for [3,4].
# The right interval for [2,3] is [3,4] since start0 = 3 is the smallest start that is >= end1 = 3.
# The right interval for [1,2] is [2,3] since start1 = 2 is the smallest start that is >= end2 = 2.
# Example 3:
#
# Input: intervals = [[1,4],[2,3],[3,4]]
# Output: [-1,2,-1]
# Explanation: There is no right interval for [1,4] and [3,4].
# The right interval for [2,3] is [3,4] since start2 = 3 is the smallest start that is >= end1 = 3.
#
#
# Constraints:
#
# 1 <= intervals.length <= 2 * 104
# intervals[i].length == 2
# -106 <= starti <= endi <= 106
# The start point of each interval is unique.
#
#
# start time:17:14
# end time: 17:40
# improvement end time: 17:47
import bisect
from typing import List

# def test_case_1():
#     intervals = [[1, 2]]
#     assert solution(intervals) == [-1]


# def test_case_2():
#     intervals = [[3,4],[2,3],[1,2]]
#     assert solution(intervals) == [-1,0,1]


# def test_case_3():
#     intervals = [[1, 4], [2, 3], [3, 4]]
#     assert solution(intervals) == [-1,2,-1]

# def test_case_4():
#     intervals = [[1,12],[2,9],[3,10],[13,14],[15,16],[16,17]]
#     assert solution(intervals) == [3,3,3,4,5,-1]

# def test_case_5():
#     intervals = [[1,1],[3,4]]
#     assert solution(intervals) == [0,-1]


def solution(intervals: List[List[int]]) -> List[int]:
    intervals_with_index = [(item, index) for index, item in enumerate(intervals)]

    # print(intervals_with_index)


    intervals_with_index.sort(key=lambda ele: ele[0][0])

    # print("sorted:", intervals_with_index)

    result = [-1] * len(intervals)

    # print(len(result))

    for i in range(len(intervals_with_index)):
        end_i = intervals_with_index[i][0][1]
        index_i = intervals_with_index[i][1]

        low = i
        high = len(intervals_with_index) - 1

        while low <= high:
            mid = low + (high - low) // 2

            if intervals_with_index[mid][0][0] < end_i:
                low = mid + 1
            else:
                high = mid - 1

        if low < len(intervals_with_index) :
            result[index_i] = intervals_with_index[low][1]


    return result

# if __name__ == '__main__':
#     test_case_1()
#     test_case_2()
#     test_case_3()
#     test_case_4()
#     test_case_5()