# https://leetcode.com/problems/interval-list-intersections/description/
#
# You are given two lists of closed intervals, firstList and secondList,
# where firstList[i] = [starti, endi] and secondList[j] = [startj, endj].
# Each list of intervals is pairwise disjoint and in sorted order.
#
# Return the intersection of these two interval lists.
#
# A closed interval [a, b] (with a <= b) denotes the set of real numbers x with a <= x <= b.
#
# The intersection of two closed intervals is a set of real numbers that are either empty
# or represented as a closed interval. For example, the intersection of [1, 3] and [2, 4] is [2, 3].
#
#
#
# Example 1:
#
#
# Input: firstList = [[0,2],[5,10],[13,23],[24,25]], secondList = [[1,5],[8,12],[15,24],[25,26]]
# Output: [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]
# Example 2:
#
# Input: firstList = [[1,3],[5,9]], secondList = []
# Output: []
#
#
# Constraints:
#
# 0 <= firstList.length, secondList.length <= 1000
# firstList.length + secondList.length >= 1
# 0 <= starti < endi <= 109
# endi < starti+1
# 0 <= startj < endj <= 109
# endj < startj+1
#
#
from typing import List

def test_case1():
    firstList = [[0, 2], [5, 10], [13, 23], [24, 25]]
    secondList = [[1, 5], [8, 12], [15, 24], [25, 26]]

    assert solution(firstList, secondList) == [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]


def test_case2():
    firstList = [[1, 3], [5, 9]]
    secondList = []

    assert solution(firstList, secondList) == []

def test_case3():
    firstList = [[1, 3], [5, 9]]
    secondList = [[5, 6]]

    assert solution(firstList, secondList) == [[5,6]]


def solution(firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
    if not firstList or not secondList:
        return []

    i = j = 0

    result = []

    while i < len(firstList) and j < len(secondList):
        low = max(firstList[i][0], secondList[j][0])
        high = min(firstList[i][1], secondList[j][1])

        if low <= high:
            result.append([low, high])

        if firstList[i][1] < secondList[j][1]:
            i += 1
        else:
            j += 1

    print(result)
    return result

if __name__ == '__main__':
    test_case1()
    test_case2()
    test_case3()




