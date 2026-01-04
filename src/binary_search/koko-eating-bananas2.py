import math
from typing import List


def test_case1():
    piles = [3, 6, 7, 11]
    h = 8

    assert solution(piles, h) == 4


def test_case2():
    piles = [30,11,23,4,20]
    h = 5

    assert solution(piles, h) == 30


def test_case3():
    piles = [30,11,23,4,20]
    h = 6

    assert solution(piles, h) == 23

def test_case4():
    piles = [312884470]
    h = 312884469

    assert solution(piles, h) == 2

def test_case5():
    piles = [2,2]
    h = 2
    assert solution(piles, h) == 2


def solution(piles: List[int], h: int) -> int:
    # speed range [k, max of piles]
    # time range  [4, y, y, 8, n, n, n] [4, 5, 6, 7, 8]

    piles.sort()

    # fastest_speed = piles[-1]
    # slowest_speed = 0

    # speeds = list(range(slowest_speed, fastest_speed + 1))

    left = 0
    right = piles[-1] ## right = max(piles)

    while left < right:
        mid = left + (right - left)//2

        sum_hours = 0
        for item in piles:
            sum_hours += math.ceil(item / mid)

        if sum_hours > h:
            left = mid + 1
        else:
            right = mid

    return left



if __name__ == '__main__':
    test_case1()
    test_case2()
    test_case3()
    test_case4()
    test_case5()




