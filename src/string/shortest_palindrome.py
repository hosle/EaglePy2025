# You are given a string s.You can convert s to a palindrome by adding characters in front of it.
# Return the shortest palindrome you can find by performing this transformation.
#
# Example 1:
# Input: s = "aacecaaa"
# Output: "aaacecaaa"

# Example 2:
# Input: s = "abcd"
# Output: "dcbabcd"
#
# Constraints:
#
# 0 <= s.length <= 5 * 104
# s consists of lowercase English letters only.

def solution(str):
    if len(str) == 1:
        return str

    i = 1
    longest_palindrome = 0

    while i < len(str):
        if is_palidrome(str[0:i]):
            longest_palindrome = max(i-1, longest_palindrome)
        i += 1

    print("longest_palindrome:", longest_palindrome)

    if longest_palindrome == len(str) - 1:
        return str

    palindrome_str = str[0:longest_palindrome+1]
    append_left = str[longest_palindrome+1:len(str)][::-1]

    print("palindrome str: ", palindrome_str)
    print("append_left:", append_left)

    result = append_left + str

    return result


def is_palidrome(str):
    i = 0
    j = len(str) - 1

    while i <= j:
        if str[i] == str[j]:
            i += 1
            j -= 1
        else:
            break

    return i >= j


if __name__ == "__main__":

    assert "a" == solution("a")

    assert "aaacecaaa" == solution("aacecaaa")

    assert "dcbabcd" == solution("abcd")