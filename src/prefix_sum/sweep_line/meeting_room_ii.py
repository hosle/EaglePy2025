# https://leetcode.com/problems/meeting-rooms-ii/description/
# 
# Given an array of meeting time intervals intervals where intervals[i] = [starti, endi], 
# return the minimum number of conference rooms required.
#
# Example 1:
# Input: intervals = [[0,30],[5,10],[15,20]]
# Output: 2
# 
# Example 2:
# Input: intervals = [[7,10],[2,4]]
# 
# Output: 1
# 
# Constraints:
# 1 <= intervals.length <= 104
# 0 <= starti < endi <= 106
#
#
from typing import List
import logging
import heapq
import math

def solution2(intervals: List[List[int]]) -> int:
    count = {}
    
    for interval in intervals:
        count[interval[0]] = count.get(interval[0], 0) + 1
        count[interval[1]+1] = count.get(interval[1]+1, 0) - 1
    
    max_count = -math.inf
    max_start = 0
    total = 0
    
    for time, amt in sorted(count.items()):
        total += amt
        
        if total > max_count:
            max_count = total
            max_start = time
    
    return max_count
    
    

def solution(intervals: List[List[int]]) -> int:

    rooms_avail_start_at = []

    heapq.heappush(rooms_avail_start_at, 0)

    intervals.sort(key = lambda interval: interval[0])

    for i in range(len(intervals)):

        if rooms_avail_start_at[0] <= intervals[i][0]:
            heapq.heappop(rooms_avail_start_at)
        
        heapq.heappush(rooms_avail_start_at, intervals[i][1])
    
        logging.debug(rooms_avail_start_at)
    
    return len(rooms_avail_start_at)