# https://leetcode.com/problems/remove-interval/description/
#
# A set of real numbers can be represented as the union of several disjoint intervals,
# where each interval is in the form [a, b). A real number x is in the set if one of its intervals [a, b) contains x (i.e. a <= x < b).
#
# You are given a sorted list of disjoint intervals intervals representing a set of real numbers as described above,
# where intervals[i] = [ai, bi] represents the interval [ai, bi). You are also given another interval toBeRemoved.
#
# Return the set of real numbers with the interval toBeRemoved removed from intervals.
# In other words, return the set of real numbers such that every x in the set is in intervals but not in toBeRemoved.
# Your answer should be a sorted list of disjoint intervals as described above.
#
# Example 1:
#
#
# Input: intervals = [[0,2],[3,4],[5,7]], toBeRemoved = [1,6]
# Output: [[0,1],[6,7]]
# Example 2:
#
#
# Input: intervals = [[0,5]], toBeRemoved = [2,3]
# Output: [[0,2],[3,5]]
# Example 3:
#
# Input: intervals = [[-5,-4],[-3,-2],[1,2],[3,5],[8,9]], toBeRemoved = [-1,4]
# Output: [[-5,-4],[-3,-2],[4,5],[8,9]]
#
# Constraints:
#
# 1 <= intervals.length <= 104
# -109 <= ai < bi <= 109

#
# start time : 16:09
# pause 12mins
# end time : 17:05

from typing import List

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


def solution(intervals: List[List[int]], toBeRemoved: List[int]) -> List[List[int]]:

    result = []

    for item in intervals:
        abstract_intervals = []

        if item[0] < toBeRemoved[0]:
            abstract_intervals.append([item[0],min(item[1], toBeRemoved[0])])

            if item[1] > toBeRemoved[1]:
                abstract_intervals.append([toBeRemoved[1],item[1]])
        else:
            if item[0] > toBeRemoved[1]:
                abstract_intervals.append(item)
            elif item[1] > toBeRemoved[1]:
                abstract_intervals.append([toBeRemoved[1], item[1]])

        if abstract_intervals:
            print(abstract_intervals)
            result.extend(abstract_intervals)

    return result


# if __name__ == '__main__':
#     test_case0()
#     # test_case1()
#     # test_case2()

