# https://leetcode.com/problems/valid-triangle-number
#
# Given an integer array nums, return the number of triplets chosen from the array that can make triangles if we take them as side lengths of a triangle.
#
#
#
# Example 1:
#
# Input: nums = [2,2,3,4]
# Output: 3
# Explanation: Valid combinations are:
# 2,3,4 (using the first 2)
# 2,3,4 (using the second 2)
# 2,2,3
# Example 2:
#
# Input: nums = [4,2,3,4]
# Output: 4
#
#
# Constraints:
#
# 1 <= nums.length <= 1000
# 0 <= nums[i] <= 1000
#
import bisect
from typing import List

def test_case1():
    assert solution([2,2,3,4]) == 3

def test_case2():
    assert solution([4,2,3,4]) == 4

def test_case3():
    assert solution([0,1,1,1]) == 1

def test_case4():
    assert solution([0,0,0]) == 0


def solution(nums: List[int]) -> int:
    n = len(nums)

    nums.sort()

    result = 0

    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            third = bisect.bisect_left(nums, nums[i] + nums[j])
            result += max(third - 1 - j, 0)

            # print("i, j, third-1:", i, j, third-1)
            # print(nums[i], nums[j], nums[third - 1])
            # print("total=", third - 1 - j)

    return result


if __name__ == "__main__":
    # test_case1()
    # test_case2()
    # test_case3()
    test_case4()
