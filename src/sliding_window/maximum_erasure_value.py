# https://leetcode.com/problems/maximum-erasure-value/description/?envType=problem-list-v2&envId=sliding-window
#
# You are given an array of positive integers nums and want to erase a subarray containing unique elements. The score you get by erasing the subarray is equal to the sum of its elements.
#
# Return the maximum score you can get by erasing exactly one subarray.
#
# An array b is called to be a subarray of a if it forms a contiguous subsequence of a, that is, if it is equal to a[l],a[l+1],...,a[r] for some (l,r).
#
#
#
# Example 1:
#
# Input: nums = [4,2,4,5,6]
# Output: 17
# Explanation: The optimal subarray here is [2,4,5,6].
# Example 2:
#
# Input: nums = [5,2,1,2,5,2,1,2,5]
# Output: 8
# Explanation: The optimal subarray here is [5,2,1] or [1,2,5].
#
#
# Constraints:
#
# 1 <= nums.length <= 105
# 1 <= nums[i] <= 104
#
# start time : 10:43
# end time : 12: 01
#
#


from typing import List

def solution (nums: List[int]) -> int:
    pre = 0
    post = 0
    n = len(nums)

    visited = set()
    result = 0
    sliding_win = 0

    # Input: nums = [4,2,4,5,6]
    while post < n:
        while nums[post] in visited:
            sliding_win -= nums[pre]
            visited.remove(nums[pre])
            pre += 1

        print("pre index= ", pre)

        sliding_win += nums[post]
        visited.add(nums[post])

        result = max(result, sliding_win)
        post += 1

    print("result=", result)
    return result




# def test_case_1():
#     nums = [4,2,4,5,6]
#     result = solution(nums)
#     print("test 1 : ", result)
#     assert(result == 17)

# def test_case_2():
#     nums = [5,2,1,2,5,2,1,2,5]
#     result = solution(nums)
#     print("test 2 : ", result)
#     assert (result == 8)

# def test_case_3():
#     nums = [5]
#     result = solution(nums)
#     print("test 3 : ", result)
#     assert (result == 5)

# def test_case_4():
#     nums = [5, 5]
#     result = solution(nums)
#     print("test 4 : ", result)
#     assert (result == 5)

# def test_case_5():
#     nums = [4,2,4,4,5,6]
#     result = solution(nums)
#     print("test 5 : ", result)
#     assert(result == 15)


# if __name__ == "__main__":
#     test_case_1()
#     test_case_2()
#     test_case_3()
#     test_case_4()
#     test_case_5()


