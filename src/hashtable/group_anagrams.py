# https://leetcode.com/problems/group-anagrams/description/?envType=problem-list-v2&envId=hash-table
from typing import List


# Given an array of strings strs, group the anagrams together. You can return the answer in any order.
#
#
#
# Example 1:
#
# Input: strs = ["eat","tea","tan","ate","nat","bat"]
#
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
#
# Explanation:
#
# There is no string in strs that can be rearranged to form "bat".
# The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
# The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.
# Example 2:
#
# Input: strs = [""]
#
# Output: [[""]]
#
# Example 3:
#
# Input: strs = ["a"]
#
# Output: [["a"]]
#
#
#
# Constraints:
#
# 1 <= strs.length <= 104
# 0 <= strs[i].length <= 100
# strs[i] consists of lowercase English letters.

# Start Time: 15:43
# End Time: 16:08
# Duration: 25mins

def solution(strs: List[str]) -> List[List[str]]:
    result = dict()

    for cur_str in strs:

        ## split string into list of characters
        sorted_arr = [c for c in cur_str]
        sorted_arr.sort()

        ## join list of characters into string
        sorted_str = ''.join(sorted_arr)

        if sorted_str not in result:
            result[sorted_str] = [cur_str]
        else:
            result[sorted_str].append(cur_str)

    print("dic = ", result)
    return list(result.values())


def test_case1():
    strs = [""]
    print(solution(strs))
    assert solution(strs) == [['']]


def test_case2():
    strs = ['a']

    assert solution(strs) == [['a']]


def compare_nested_sorted(list1, list2):
    # Sort inner lists first
    sorted_l1_inner = [sorted(inner) for inner in list1]
    sorted_l2_inner = [sorted(inner) for inner in list2]
    # Sort the outer list of sorted inner lists and compare
    return sorted(sorted_l1_inner) == sorted(sorted_l2_inner)


def test_case3():
    strs = ["eat","tea","tan","ate","nat","bat"]
    print("result =", solution(strs))
    assert compare_nested_sorted(solution(strs),[["bat"],["nat","tan"],["ate","eat","tea"]])

if __name__ == "__main__":
    test_case1()
    test_case2()
    test_case3()