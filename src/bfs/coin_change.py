# https://leetcode.com/problems/coin-change/description/
# You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.
# Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.
# You may assume that you have an infinite number of each kind of coin.
# Example 1:
# Input: coins = [1,2,5], amount = 11
# Output: 3
# Explanation: 11 = 5 + 5 + 1
# Example 2:
# Input: coins = [2], amount = 3
# Output: -1
# Example 3:
# Input: coins = [1], amount = 0
# Output: 0
# Constraints:
# 1 <= coins.length <= 12
# 1 <= coins[i] <= 231 - 1
# 0 <= amount <= 104
#
#
#
# 
from typing import List
import bisect
# TODO change to Dynamic Programming
def solution(coins: List[int], amount: int) -> int:
    coins.sort()
    n = len(coins)
    
    if amount == 0:
        return 0
    
    count = 0
    
    while amount > 0:
        index = bisect.bisect_left(coins, amount)
        print(f"{index=}")
        count += 1
        
        if index < n and amount == coins[index]:
            return count
        else:
            index -= 1
            amount -= coins[index]
        
    return -1
    