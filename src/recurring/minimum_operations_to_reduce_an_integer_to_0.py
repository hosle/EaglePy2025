# https://leetcode.com/problems/minimum-operations-to-reduce-an-integer-to-0/description/
#
# You are given a positive integer n, you can do the following operation any number of times:
# Add or subtract a power of 2 from n.
# Return the minimum number of operations to make n equal to 0.
#
# A number x is power of 2 if x == 2i where i >= 0.
#
# Example 1:
#
# Input: n = 39
# Output: 3
# Explanation: We can do the following operations:
# - Add 20 = 1 to n, so now n = 40.
# - Subtract 23 = 8 from n, so now n = 32.
# - Subtract 25 = 32 from n, so now n = 0.
# It can be shown that 3 is the minimum number of operations we need to make n equal to 0.
# Example 2:
#
# Input: n = 54
# Output: 3
# Explanation: We can do the following operations:
# - Add 21 = 2 to n, so now n = 56.
# - Add 23 = 8 to n, so now n = 64.
# - Subtract 26 = 64 from n, so now n = 0.
# So the minimum number of operations is 3.
#
#
# Constraints:
#
# 1 <= n <= 105
# start time : 10:59am
# end time:11:28am

# def test_case1():
#     n = 39
#     assert solution(n) == 3


# def test_case2():
#     n = 54
#     assert solution(n) == 3


def solution(n: int) -> int:
    count = 0
    
    def count_diff(input: int) -> int:
        nonlocal count
        if input == 0:
            return
        
        acc = 1
        while acc < input:
            acc *= 2
        diff = abs(acc - input)
        diff_last = abs(acc//2 - input)
        
        # print("diff: ", diff)
        # print("diff_last: ", diff_last)

        count += 1

        return count_diff(min(diff,diff_last))
    
    count_diff(n)

    return count


# if __name__ == '__main__':
#     test_case1()
#     test_case2()