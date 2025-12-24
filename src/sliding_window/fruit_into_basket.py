# https://leetcode.com/problems/fruit-into-baskets
#
# You are visiting a farm that has a single row of fruit trees arranged from left to right. The trees are represented by an integer array fruits where fruits[i] is the type of fruit the ith tree produces.
#
# You want to collect as much fruit as possible. However, the owner has some strict rules that you must follow:
#
# You only have two baskets, and each basket can only hold a single type of fruit. There is no limit on the amount of fruit each basket can hold.
# Starting from any tree of your choice, you must pick exactly one fruit from every tree (including the start tree) while moving to the right. The picked fruits must fit in one of your baskets.
# Once you reach a tree with fruit that cannot fit in your baskets, you must stop.
# Given the integer array fruits, return the maximum number of fruits you can pick.
#
#
#
# Example 1:
#
# Input: fruits = [1,2,1]
# Output: 3
# Explanation: We can pick from all 3 trees.
# Example 2:
#
# Input: fruits = [0,1,2,2]
# Output: 3
# Explanation: We can pick from trees [1,2,2].
# If we had started at the first tree, we would only pick from trees [0,1].
# Example 3:
#
# Input: fruits = [1,2,3,2,2]
# Output: 4
# Explanation: We can pick from trees [2,3,2,2].
# If we had started at the first tree, we would only pick from trees [1,2].
#
#
# Constraints:
#
# 1 <= fruits.length <= 105
# 0 <= fruits[i] < fruits.length

from typing import List

def test_case1():
    result = solution([1,2,1])
    print(result)
    assert result == 3


def test_case2():
    result = solution([0,1,2,2])
    print(result)
    assert result == 3

def test_case3():
    result = solution([1,2,3,2,2])
    print(result)
    assert result == 4

def test_case4():
    result = solution([1])
    print(result)
    assert result == 1

def test_case5():
    result = solution([1,2])
    print(result)
    assert result == 2

def test_case6():
    result = solution([1, 1])
    print(result)
    assert result == 2

def test_case7():
    result = solution([1, 2, 1])
    print(result)
    assert result == 3

def test_case8():
    result = solution([1, 2, 3])
    print(result)
    assert result == 2


def solution(fruits: List[int]) -> int:
    pre = 0
    post = 0

    fruit_count = dict()

    result = 0

    while post < len(fruits):
        fruit_count[fruits[post]] = fruit_count.get(fruits[post], 0) + 1

        while len(fruit_count) > 2:
            fruit_count[fruits[pre]] -= 1

            if fruit_count[fruits[pre]] == 0:

                # better practice to delete key from a dict
                try:
                    del fruit_count[fruits[pre]]
                except KeyError:
                    print("Key not found!")
                # alternative : fruit_count.pop(fruits[pre])

            pre += 1

        result = max(result, post - pre + 1)

        post += 1

    return result


if __name__ == '__main__':
    test_case1()
    test_case2()
    test_case3()
    test_case4()
    test_case5()
    test_case6()
    test_case7()
    test_case8()

