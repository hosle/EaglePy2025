# https://leetcode.com/problems/maximum-frequency-of-an-element-after-performing-operations-i/
#
# You are given an integer array nums and two integers k and numOperations.
# You must perform an operation numOperations times on nums, where in each operation you:
# Select an index i that was not selected in any previous operations.
# Add an integer in the range [-k, k] to nums[i].
# Return the maximum possible frequency of any element in nums after performing the operations.
# 
# Example 1:
# Input: nums = [1,4,5], k = 1, numOperations = 2
# Output: 2
# Explanation:
# We can achieve a maximum frequency of two by:
# Adding 0 to nums[1]. nums becomes [1, 4, 5].
# Adding -1 to nums[2]. nums becomes [1, 4, 4].
# 
# Example 2:
# Input: nums = [5,11,20,20], k = 5, numOperations = 1
# Output: 2
# Explanation:
# We can achieve a maximum frequency of two by:
# Adding 0 to nums[1].
# Constraints:
# 1 <= nums.length <= 105
# 1 <= nums[i] <= 105
# 0 <= k <= 105
# 0 <= numOperations <= nums.length
#
# start time : 1:33pm
# pause : 1:34pm
# resume : 1:38pm
# end time : 3:17pm
#
from typing import List
import logging
import bisect
from collections import Counter

def solution(nums: List[int], k: int, numOperations: int) -> int:
    
    nums.sort()
    
    post = 0
    pre = 0
    n = len(nums)
    result = 0
    pre_sum = 0
    
    cnt = Counter(nums)
    
    while post < n:
        while pre < post and (nums[post] - nums[pre] > 2 * k or post - pre + 1> numOperations):
            pre += 1
        
        result = max(result, post - pre + 1)
        
        post += 1
    
    logging.debug(result)
    
    for item in nums:
        most_left = bisect.bisect_left(nums, item - k)
        most_right = bisect.bisect_right(nums, item + k)
        logging.debug(f"{most_left=},{most_right=} ")
        
        c = cnt[item]
        result = max(result, c + min(numOperations, most_right - most_left - c))
    
    return result
    
    