# https://leetcode.com/problems/find-k-closest-elements
#
#
# Given a sorted integer array arr, two integers k and x, return the k closest integers to x in the array.
# The result should also be sorted in ascending order.
#
# An integer a is closer to x than an integer b if:
#
# |a - x| < |b - x|, or
# |a - x| == |b - x| and a < b
#
#
# Example 1:
#
# Input: arr = [1,2,3,4,5], k = 4, x = 3
#
# Output: [1,2,3,4]
#
# Example 2:
#
# Input: arr = [1,1,2,3,4,5], k = 4, x = -1
#
# Output: [1,1,2,3]
#
#
#
# Constraints:
#
# 1 <= k <= arr.length
# 1 <= arr.length <= 104
# arr is sorted in ascending order.
# -104 <= arr[i], x <= 104
from bisect import bisect_left
from typing import List
import heapq
import sys

def test_case1():
    result = solution4([1,2,3,4,5], 4, 3)
    print(result)
    assert result == [1,2,3,4]


def test_case2():
    result = solution4([1,1,2,3,4,5], 4, -1)
    print(result)
    assert result == [1, 1, 2, 3]

def test_case3():
    result = solution4([1,1,1,10,10,10], 1, 9)
    print(result)
    assert result == [10]

def test_case4():
    result = solution4([0,1,1,1,2,3,6,7,8,9], 9, 4)
    print(result)
    assert result == [0,1,1,1,2,3,6,7,8]


def solution4(arr: List[int], k: int, x: int) -> List[int]:
    if k == len(arr):
        return arr

    post = bisect_left(arr, x)

    pre = post - 1

    while post - pre - 1 < k:
        if pre == -1:
            post += 1
            continue

        if post == len(arr) or abs(arr[post] - x) >= abs(arr[pre] - x):
            pre -= 1
        else:
            post += 1


    return arr[pre+1:post]





def solution3(arr: List[int], k: int, x: int) -> List[int]:
    if k == len(arr):
        return arr

    # Every time you see a problem that involves a sorted array, you should consider binary search.
    pre = bisect_left(arr, x) - 1

    post = pre + 1

    while post - pre - 1 < k:
        if pre == -1:
            post += 1
            continue

        if post == len(arr):
            pre -= 1
            continue

        if abs(arr[post] - x) >= abs(arr[pre] - x):
            pre -= 1
        else:
            post += 1

    return arr[pre+1:post]



def solution2(arr: List[int], k: int, x: int) -> List[int]:
    diff_sum = 0

    pre = 0
    post = 0
    result = []
    min_diff = sys.maxsize

    while post < len(arr):
        diff_sum += abs(arr[post] - x)

        while post - pre + 1 > k:
            diff_sum -= abs(arr[pre] - x)
            pre += 1

        print(f"diff_sum = {diff_sum}, min_diff = {min_diff}")

        if diff_sum < min_diff and post - pre + 1 == k:
            min_diff = diff_sum
            result = arr[pre:post+1]

        post += 1

    return result


def solution(arr: List[int], k: int, x: int) -> List[int]:
    arr_with_diff = [(abs(item - x), item) for item in arr]

    heapq.heapify(arr_with_diff)

    result = []

    for i in range(k):
        result.append(heapq.heappop(arr_with_diff)[1])

    result.sort()

    return result


if __name__ == "__main__":
    test_case1()
    test_case2()
    test_case3()
    test_case4()


