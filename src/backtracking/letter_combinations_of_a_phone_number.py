# https://leetcode.com/problems/letter-combinations-of-a-phone-number/
# Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.
# A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.
# Example 1:
# Input: digits = "23"
# Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
# Example 2:
# Input: digits = "2"
# Output: ["a","b","c"]
# Constraints:
# 1 <= digits.length <= 4
# digits[i] is a digit in the range ['2', '9'].

from typing import List

def solution(digits: str) -> List[str]:
    num_dict = {
        "2":["a","b","c"],
        "3":["d","e","f"],
        "4":["g","h","i"],
        "5":["j","k","l"],
        "6":["m","n","o"],
        "7":["p","q","r","s"],
        "8":["t","u","v"],
        "9":["w","x","y","z"]
    }
    
    result = []
    
    if not digits:
        return []
    
    n = len(digits)
    
    def backtracking(path, index):
        nonlocal n
        if index == n:
            result.append("".join(path))
            print(f"{result=}")
            return
        
        for i, item in enumerate(num_dict[digits[index]]):
            path.append(item)
            backtracking(path, index + 1)
            path.pop()
    
    backtracking([], 0)
    
    return result