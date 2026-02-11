# https://leetcode.com/problems/partition-array-into-disjoint-intervals/description/
#
#
# Given an integer array nums, partition it into two (contiguous) subarrays left and right so that:
#
# Every element in left is less than or equal to every element in right.
# left and right are non-empty.
# left has the smallest possible size.
# Return the length of left after such a partitioning.
#
# Test cases are generated such that partitioning exists.
#
#
# Example 1:
#
# Input: nums = [5,0,3,8,6]
# Output: 3
# Explanation: left = [5,0,3], right = [8,6]
# Example 2:
#
# Input: nums = [1,1,1,0,6,12]
# Output: 4
# Explanation: left = [1,1,1,0], right = [6,12]
# Constraints:
#
# 2 <= nums.length <= 10^5
# 0 <= nums[i] <= 10^6
# There is at least one valid answer for the given input.
#
# def test_case1():
#     nums = [5,0,3,8,6]
#     assert solution(nums) == 3
# def test_case2():
#     nums = [1,1,1,0,6,12]
#     assert solution(nums) == 4

from typing import List

def solution(nums: List[int]) -> int:
    max_lefts = [0] * len(nums)
    max_lefts[0] = nums[0]
    min_rights = [0] * len(nums)
    min_rights[-1] = nums[-1]

    for i in range(1, len(nums)):
        max_lefts[i] = max(max_lefts[i-1], nums[i])

    # print(max_lefts)

    for j in range(len(nums)-2, -1, -1):
        min_rights[j] = min(min_rights[j+1], nums[j])

    # print(min_rights)

    for i in range(len(nums)-1):
        if max_lefts[i] <= min_rights[i+1]:
            return i+1
    return 0

# if __name__ == '__main__':
#     test_case1()
#     test_case2()

