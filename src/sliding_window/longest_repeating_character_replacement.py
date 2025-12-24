# https://leetcode.com/problems/longest-repeating-character-replacement/description/
#
#
# You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.
#
# Return the length of the longest substring containing the same letter you can get after performing the above operations.
#
#
#
# Example 1:
#
# Input: s = "ABAB", k = 2
# Output: 4
# Explanation: Replace the two 'A's with two 'B's or vice versa.
# Example 2:
#
# Input: s = "AABABBA", k = 1
# Output: 4
# Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
# The substring "BBBB" has the longest repeating letters, which is 4.
# There may exists other ways to achieve this answer too.
#
#
# Constraints:
#
# 1 <= s.length <= 105
# s consists of only uppercase English letters.
# 0 <= k <= s.length
import heapq


# start time 12:02
# end time 13:11

def test_case1():
    result = solution("ABAB",2)
    print(result)
    assert result == 4


def test_case2():
    result = solution("AABABBA", 1)
    print(result)
    assert result == 4


def test_case3():
    result = solution("AAAAAAA", 1)
    print(result)
    assert result == 7


def test_case4():
    result = solution("ABBAACA", 2)
    print(result)
    assert result == 5


def solution (s: str, k: int) -> int:
    pre = 0
    post = 0

    count_alpha = dict()
    result = 0

    def is_exceed_k_diff(_pre, _post):
        max_value = 0
        for key,value in count_alpha.items():
            max_value = max(max_value, value)

        return _post - _pre + 1 - max_value > k


    while post < len(s):
        count_alpha[s[post]] = count_alpha.get(s[post], 0) + 1

        while is_exceed_k_diff(pre, post):
            next_count = count_alpha[s[pre]] - 1
            count_alpha[s[pre]] = next_count
            pre += 1

        # print(f"pre = {pre}, post = {post}, dict_alpha = {count_alpha}")

        result = max(result, post - pre + 1)

        post += 1

    return result


if __name__ == '__main__':
    test_case1()
    test_case2()
    test_case3()
    test_case4()
