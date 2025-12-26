# https://leetcode.com/problems/find-all-anagrams-in-a-string/description/
#
# Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.
#
# Example 1:
#
# Input: s = "cbaebabacd", p = "abc"
# Output: [0,6]
# Explanation:
# The substring with start index = 0 is "cba", which is an anagram of "abc".
# The substring with start index = 6 is "bac", which is an anagram of "abc".
# Example 2:
#
# Input: s = "abab", p = "ab"
# Output: [0,1,2]
# Explanation:
# The substring with start index = 0 is "ab", which is an anagram of "ab".
# The substring with start index = 1 is "ba", which is an anagram of "ab".
# The substring with start index = 2 is "ab", which is an anagram of "ab".
#
#
# Constraints:
#
# 1 <= s.length, p.length <= 3 * 104
# s and p consist of lowercase English letters.
#
from collections import deque
from typing import List

def test_case1():
    result = solution("cbaebabacd", "abc")
    print(result)
    assert result == [0,6]


def test_case2():
    result = solution("abab", "ab")
    print(result)
    assert result == [0,1,2]


def test_case3():
    result = solution("aaabb", "bb")
    print(result)
    assert result == [3]


def solution(s: str, p: str) -> List[int]:
    ori_map = {}
    for str_p in p:
        ori_map[str_p] = ori_map.get(str_p, 0) + 1

    cur_map = {}

    post = 0
    result = []

    np = len(p)

    while post < len(s):

        cur_map[s[post]] =  cur_map.get(s[post], 0) + 1

        if post >= np:
            if cur_map[s[post-np]] == 1:
                del cur_map[s[post-np]]
            else:
                cur_map[s[post-np]] -= 1

        if cur_map == ori_map:
            result.append(post -np + 1)

        post += 1

    return result



if __name__ == '__main__':
    test_case1()
    test_case2()
    test_case3()