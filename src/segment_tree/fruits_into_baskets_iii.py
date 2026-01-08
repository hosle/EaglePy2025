# https://leetcode.com/problems/fruits-into-baskets-iii/description/

# You are given two arrays of integers, fruits and baskets, each of length n, 
# where fruits[i] represents the quantity of the ith type of fruit, 
# and baskets[j] represents the capacity of the jth basket.

# From left to right, place the fruits according to these rules:

# Each fruit type must be placed in the leftmost available basket with 
# a capacity greater than or equal to the quantity of that fruit type.
# Each basket can hold only one type of fruit.
# If a fruit type cannot be placed in any basket, it remains unplaced.
# Return the number of fruit types that remain unplaced after all possible 
# allocations are made.

 

# Example 1:

# Input: fruits = [4,2,5], baskets = [3,5,4]

# Output: 1

# Explanation:

# fruits[0] = 4 is placed in baskets[1] = 5.
# fruits[1] = 2 is placed in baskets[0] = 3.
# fruits[2] = 5 cannot be placed in baskets[2] = 4.
# Since one fruit type remains unplaced, we return 1.

# Example 2:

# Input: fruits = [3,6,1], baskets = [6,4,7]

# Output: 0

# Explanation:

# fruits[0] = 3 is placed in baskets[0] = 6.
# fruits[1] = 6 cannot be placed in baskets[1] = 4 (insufficient capacity) but can be placed in the next available basket, baskets[2] = 7.
# fruits[2] = 1 is placed in baskets[1] = 4.
# Since all fruits are successfully placed, we return 0.

 

# Constraints:

# n == fruits.length == baskets.length
# 1 <= n <= 105
# 1 <= fruits[i], baskets[i] <= 109
# 
# start time: 17:16
# end time: 18:04 fail test cases

# learn segment tree

from typing import List
from collections import deque
import logging

# def test_case1():
#     fruits = [4,2,5]
#     baskets = [3,5,4]
#     assert solution(fruits, baskets) == 1


# def test_case2():
#     fruits = [3,6,1]
#     baskets = [6,4,7]
#     assert solution(fruits, baskets) == 0


# def test_case2():
#     fruits = [4,5,6]
#     baskets = [1,2,3]
#     assert solution(fruits, baskets) == 3


# def test_case3():
#     fruits = [1,3,3]
#     baskets = [1,2,6]
#     assert solution(fruits, baskets) == 1

# def test_case4():
#     fruits = [20,8]
#     baskets = [79,4]
#     assert solution(fruits, baskets) == 1




class SegTree:
    def __init__(self, input_arr:List[int]):
        self.n = len(input_arr)
        size = 2 << (self.n - 1).bit_length()
        # print("bit length:", (self.n - 1).bit_length())
        logging.debug(f"bit length:{(self.n - 1).bit_length()}")
        # print("size: ", size)
        logging.debug(f"size: {size}")
        print(size, "size")
        
        self.seg = [0] * size

        self._build(input_arr, 1, 0, self.n-1)
        
    def _build(self, input_array, start, left, right):
        if left == right:
            self.seg[start] = input_array[left]
            return
        
        mid = (left + right )//2

        self._build(input_array, start * 2, left, mid)
        self._build(input_array, start * 2 + 1, mid + 1, right)
        self._maintain(start)
    
    def _maintain(self, start):
        self.seg[start] = max(self.seg[start*2], self.seg[start*2+1])
    
    def _find_first_and_update(self, start, left, right, target):
        if self.seg[start] < target:
            return -1
        
        if left == right:
            self.seg[start] = -1
            return left
        
        mid = (left + right) // 2

        i = self._find_first_and_update(start*2, left, mid, target)
        if i == -1:
            i = self._find_first_and_update(start*2+1, mid+1, right, target)

        self._maintain(start)

        return i


def solution(fruits: List[int], baskets: List[int]) -> int:
    m = len(baskets)

    if m == 0:
        return len(fruits)
    
    tree = SegTree(baskets)
    # print(tree.seg)
    logging.debug(tree.seg)

    count = 0

    for fruit in fruits:
        if tree._find_first_and_update(1, 0, m-1, fruit) == -1:
            count += 1
    
    return count

# if __name__ == '__main__':
    # test_case1()
    # test_case2()
    # test_case3()
    # test_case4()


