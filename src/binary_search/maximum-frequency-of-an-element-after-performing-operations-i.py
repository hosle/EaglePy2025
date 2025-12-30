# https://leetcode.com/problems/maximum-frequency-of-an-element-after-performing-operations-i/description/?envType=problem-list-v2&envId=binary-search
#
# You are given an integer array nums and two integers k and numOperations.
#
# You must perform an operation numOperations times on nums, where in each operation you:
#
# Select an index i that was not selected in any previous operations.
# Add an integer in the range [-k, k] to nums[i].
# Return the maximum possible frequency of any element in nums after performing the operations.
#
#
#
# Example 1:
#
# Input: nums = [1,4,5], k = 1, numOperations = 2
#
# Output: 2
#
# Explanation:
#
# We can achieve a maximum frequency of two by:
#
# Adding 0 to nums[1]. nums becomes [1, 4, 5].
# Adding -1 to nums[2]. nums becomes [1, 4, 4].
# Example 2:
#
# Input: nums = [5,11,20,20], k = 5, numOperations = 1
#
# Output: 2
#
# Explanation:
#
# We can achieve a maximum frequency of two by:
#
# Adding 0 to nums[1].
#
#
# Constraints:
#
# 1 <= nums.length <= 105
# 1 <= nums[i] <= 105
# 0 <= k <= 105
# 0 <= numOperations <= nums.length
import bisect
from typing import List

def test_case1():
    result = solution([1,4,5], 1,2)
    print(result)
    assert result == 2


def test_case2():
    result = solution([5,11,20,20], 5, 1)
    print(result)
    assert result == 2

def test_case3():
    result = solution([5], 7, 0)
    print(result)
    assert result == 1

def test_case4():
    result = solution([2, 49], 97, 0)
    print(result)
    assert result == 1


def solution(nums: List[int], k: int, numOperations: int) -> int:
    for i in range(nums[0], nums[-1] + 1):
        l = bisect.bisect_left(nums, i - k)
        r = bisect.bisect_right(nums, i + k) - 1
        print(f"i={i}, i-k={i-k}, i+k={i+k}, l={l}, r={r}")

if __name__ == '__main__':
    test_case1()
    # test_case2()
    # test_case3()
    # test_case4()

