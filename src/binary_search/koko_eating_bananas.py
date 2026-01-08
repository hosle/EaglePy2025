# https://leetcode.com/problems/koko-eating-bananas
#
# Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas.
# The guards have gone and will come back in h hours.
#
# Koko can decide her bananas-per-hour eating speed of k.
# Each hour, she chooses some pile of bananas and eats k bananas from that pile.
# If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.
#
# Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.
#
# Return the minimum integer k such that she can eat all the bananas within h hours.
#
#
#
# Example 1:
# Input: piles = [3,6,7,11], h = 8
# Output: 4
#
# Example 2:
# Input: piles = [30,11,23,4,20], h = 5
# Output: 30
#
# Example 3:
# Input: piles = [30,11,23,4,20], h = 6
# Output: 23
#
#
# Constraints:
#
# 1 <= piles.length <= 104
# piles.length <= h <= 109
# 1 <= piles[i] <= 109
import math
from typing import List
import pytest
import logging

# def test_case1():
#     assert solution([3,6,7,11], 8) == 4

# def test_case2():
#     assert solution([30,11,23,4,20], 5) == 30

# def test_case3():
#     assert solution([30,11,23,4,20], 6) == 23



def solution(piles: List[int], h: int) -> int:
    left = 1
    right = max(piles)

    while left < right:
        speed = (left + right ) // 2

        logging.debug(f"speed is {speed}")

        hour_spend = 0

        for pile_item in piles:
            hour_spend += math.ceil(pile_item / speed)

        if hour_spend > h:
            left = speed + 1
        else:
            right = speed

    return right

if __name__ == '__main__':
    test_case1()
    test_case2()
    test_case3()