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