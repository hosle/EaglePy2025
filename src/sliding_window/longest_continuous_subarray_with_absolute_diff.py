# https://leetcode.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/description
#
#
# Given an array of integers nums and an integer limit, return the size of the longest non-empty subarray
# such that the absolute difference between any two elements of this subarray is less than or equal to limit.
#
#
#
# Example 1:
#
# Input: nums = [8,2,4,7], limit = 4
# Output: 2
# Explanation: All subarrays are:
# [8] with maximum absolute diff |8-8| = 0 <= 4.
# [8,2] with maximum absolute diff |8-2| = 6 > 4.
# [8,2,4] with maximum absolute diff |8-2| = 6 > 4.
# [8,2,4,7] with maximum absolute diff |8-2| = 6 > 4.
# [2] with maximum absolute diff |2-2| = 0 <= 4.
# [2,4] with maximum absolute diff |2-4| = 2 <= 4.
# [2,4,7] with maximum absolute diff |2-7| = 5 > 4.
# [4] with maximum absolute diff |4-4| = 0 <= 4.
# [4,7] with maximum absolute diff |4-7| = 3 <= 4.
# [7] with maximum absolute diff |7-7| = 0 <= 4.
# Therefore, the size of the longest subarray is 2.
# Example 2:
#
# Input: nums = [10,1,2,4,7,2], limit = 5
# Output: 4
# Explanation: The subarray [2,4,7,2] is the longest since the maximum absolute diff is |2-7| = 5 <= 5.
# Example 3:
#
# Input: nums = [4,2,2,2,4,4,2,2], limit = 0
# Output: 3
#
#
# Constraints:
#
# 1 <= nums.length <= 105
# 1 <= nums[i] <= 109
# 0 <= limit <= 109
from collections import deque
from typing import List

# def test_case1():
#     result = solution([8,2,4,7], 4)
#     print(result)
#     assert result == 2


# def test_case2():
#     result = solution([10,1,2,4,7,2], 5)
#     print(result)
#     assert result == 4


# def test_case3():
#     result = solution([4,2,2,2,4,4,2,2], 0)
#     print(result)
#     assert result == 3


def solution(nums: List[int], limit: int) -> int:

    pre = 0
    post = 0
    result = 0
    max_queue = deque()
    min_queue = deque()


    while post < len(nums):
        while max_queue and max_queue[-1] < nums[post]:
            max_queue.pop()
        max_queue.append(nums[post])

        while min_queue and min_queue[-1] > nums[post]:
            min_queue.pop()
        min_queue.append(nums[post])

        diff = max_queue[0] - min_queue[0]

        while diff > limit:
            if min_queue[0] == nums[pre]:
                min_queue.popleft()

            if max_queue[0] == nums[pre]:
                max_queue.popleft()

            diff = max_queue[0] - min_queue[0]
            pre += 1

        result = max(result, post - pre + 1)

        post += 1

    return result


# if __name__ == '__main__':
#     test_case1()
#     test_case2()