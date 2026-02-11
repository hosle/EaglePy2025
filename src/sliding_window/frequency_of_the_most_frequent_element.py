# https://leetcode.com/problems/frequency-of-the-most-frequent-element/description/
#
# The frequency of an element is the number of times it occurs in an array.
#
# You are given an integer array nums and an integer k. In one operation, 
# you can choose an index of nums and increment the element at that index by 1.
#
# Return the maximum possible frequency of an element after performing at most k operations.
#
#
#
# Example 1:
#
# Input: nums = [1,2,4], k = 5
# Output: 3
# Explanation: Increment the first element three times and the second element two times to make nums = [4,4,4].
# 4 has a frequency of 3.
# 
# Example 2:
#
# Input: nums = [1,4,8,13], k = 5
# Output: 2
# Explanation: There are multiple optimal solutions:
# - Increment the first element three times to make nums = [4,4,8,13]. 4 has a frequency of 2.
# - Increment the second element four times to make nums = [1,8,8,13]. 8 has a frequency of 2.
# - Increment the third element five times to make nums = [1,4,13,13]. 13 has a frequency of 2.
# 
# Example 3:
#
# Input: nums = [3,9,6], k = 2
# Output: 1
#
#
# Constraints:
#
# 1 <= nums.length <= 105
# 1 <= nums[i] <= 105
# 1 <= k <= 105
#
# start time: 16:42
# end time:
#
#
# The real decision: what do you do when the window is “invalid”?
#
# If invalid means “too much stuff” (too many distinct, sum too big, freq too high)
# → shrink (left++) until valid.
#
# If invalid means “not enough yet” (haven’t covered all chars, sum too small)
# → you generally expand (right++) to try to become valid.
#
# So:
#
# Need more to satisfy → move right
#
# Need less to satisfy → move left


from typing import List

def solution(nums: List[int], k: int) -> int:
    nums.sort()
    pre = 0
    post = 0
    result = 0
    window = 0

    while post < len(nums):
        window += nums[post]

        while nums[post] * (post - pre + 1) - window > k:
            window -= nums[pre]
            pre += 1

        result = max(result, post - pre + 1)

        post += 1

    return result


# def test_case1():
#     nums = [1,2,4]
#     result = solution(nums, 5)
#     print(result)
#     assert result == 3

# def test_case2():
#     nums = [1,4,8,13]
#     result = solution(nums, 5)
#     print(result)
#     assert result == 2

# def test_case3():
#     nums = [3,9,6]
#     result = solution(nums, 2)
#     print(result)
#     assert result == 1

# if __name__ == '__main__':
#     test_case1()
#     test_case2()
#     test_case3()