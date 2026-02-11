# https://leetcode.com/problems/generate-parentheses/description/
#
#
# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
# Example 1:
# Input: n = 3
# Output: ["((()))","(()())","(())()","()(())","()()()"]
# Example 2:
# Input: n = 1
# Output: ["()"]
# Constraints:
# 1 <= n <= 8
#
#
from typing import List

def solution(n: int) -> List[str]:
    
    result = []
    
    def combination(taken, left_count, right_count):
        nonlocal n
        
        if len(taken) == 2 * n:
            result.append("".join(taken))
            return
        
        if left_count < n:
            taken.append("(")
            combination(taken, left_count+1, right_count)
            taken.pop()
        
        if right_count < left_count:
            taken.append(")")
            combination(taken, left_count, right_count + 1)
            taken.pop()
        
    
    combination([], 0, 0)
    
    return result
        
        
         