# https://leetcode.com/problems/subarray-sum-equals-k/description/
#
# Given an array of integers nums and an integer k, 
# return the total number of subarrays whose sum equals to k.
#
# A subarray is a contiguous non-empty sequence of elements within an array.
#
# Example 1:
#
# Input: nums = [1,1,1], k = 2
# Output: 2
# 
# Example 2:
#
# Input: nums = [1,2,3], k = 3
# Output: 2
# 
#
# Constraints:
#
# 1 <= nums.length <= 2 * 104
# -1000 <= nums[i] <= 1000
# -107 <= k <= 107
#
from typing import List
import logging

def solution2(nums: List[int], k: int) -> int: 
    count_dict ={0:1}
    
    pre_sum = 0
    count = 0
    
    for num in nums:
        pre_sum += num 
       
        left_sum = pre_sum - k
               
        if left_sum in count_dict:
            count += count_dict[left_sum]
        
        count_dict[pre_sum] = count_dict.get(pre_sum,0) + 1
        
    return count
            
    

def solution(nums: List[int], k: int) -> int:        
    n = len(nums)
    sum_subarrays = [0] * (n+1)
    result = 0
    
    for i in range(1, n+1):
        sum_subarrays[i] = sum_subarrays[i-1] + nums[i-1]
    
    # pre_sum = 0
    # for num in nums:
    #     pre_sum += num
    #     sum_subarrays.append(pre_sum)
    
        
    for i in range(n):
        for j in range(i+1, n+1):
            if sum_subarrays[j] - sum_subarrays[i] == k:
                result += 1
    
    return result
        