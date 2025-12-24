# https://leetcode.com/problems/max-consecutive-ones-iii
#
# Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.
#
#
#
# Example 1:
#
# Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
# Output: 6
# Explanation: [1,1,1,0,0,1,1,1,1,1,1]
# Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
# Example 2:
#
# Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
# Output: 10
# Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
# Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
#
#
# Constraints:
#
# 1 <= nums.length <= 105
# nums[i] is either 0 or 1.
# 0 <= k <= nums.length
from typing import List

def test_case1():
    result = solution([1,1,1,0,0,0,1,1,1,1,0], 2)
    print(result)
    assert result == 6


def test_case2():
    result = solution([0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], 3)
    print(result)
    assert result == 10

def test_case3():
    result = solution([1], 1)
    print(result)
    assert result == 1

def test_case4():
    result = solution([0], 1)
    print(result)
    assert result == 1


def test_case5():
    result = solution([1], 0)
    print(result)
    assert result == 1


def test_case6():
    result = solution([0], 0)
    print(result)
    assert result == 0


def solution(nums: List[int], k: int) -> int:
    pre = 0
    post = 0

    count_of_0 = 0

    result = 0

    while post < len(nums):

        if nums[post] == 0:
            count_of_0 += 1

        while count_of_0 > k:
            if nums[pre] == 0:
                count_of_0 -= 1
            pre += 1

        result = max(result, post - pre + 1)

        post += 1

    return result



if __name__ == '__main__':
    test_case1()
    test_case2()
    test_case3()
    test_case4()
    test_case5()
    test_case6()