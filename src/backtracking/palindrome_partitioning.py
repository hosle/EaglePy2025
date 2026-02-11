# https://leetcode.com/problems/palindrome-partitioning/
#
#
#Given a string s, partition s such that every substring of the partition is a palindrome. Return all possible palindrome partitioning of s.
# Example 1:
# Input: s = "aab"
# Output: [["a","a","b"],["aa","b"]]
# Example 2:
# Input: s = "a"
# Output: [["a"]]
# Constraints:
# 1 <= s.length <= 16
# s contains only lowercase English letters.

from typing import List

def solution2(s:str) -> List[List[str]]:
    
    result = []
    
    def is_palindrome(ori) -> bool:
        return ori == ori[::-1]
    
    def backtracking(path, index_start):
        
        if index_start == len(s):
            result.append(path[:])
            return        
        
        temp = ""
        for j in range(index_start, len(s)):
            temp += s[j]
            if is_palindrome(temp):
                path.append(temp)
                backtracking(path, j+1)
                path.pop()
            
    
    backtracking([], 0)
    
    print(f"{result=}")
    
    return result
    


def solution(s: str) -> List[List[str]]:
    
    def is_palindrome(input_s)->bool:
        return input_s == input_s[::-1]

    result = []
    
    def backtracking(path, index):
        if index == len(s):
            result.append(path[:])
            return
        
        temp = ""
        for i in range(index, len(s)):
            temp +=s[i]
            if is_palindrome(temp):
                path.append(temp)
                backtracking(path, i + 1)
                path.pop()
    
    backtracking([], 0)
    
    return result
            
            
        
        