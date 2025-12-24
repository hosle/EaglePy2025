# https://leetcode.com/problems/new-21-game/description/
#
# Alice plays the following game, loosely based on the card game "21".
#
# Alice starts with 0 points and draws numbers while she has less than k points. During each draw, she gains an integer number of points randomly from the range [1, maxPts], where maxPts is an integer. Each draw is independent and the outcomes have equal probabilities.
#
# Alice stops drawing numbers when she gets k or more points.
#
# Return the probability that Alice has n or fewer points.
#
# Answers within 10-5 of the actual answer are considered accepted.
#
#
#
# Example 1:
#
# Input: n = 10, k = 1, maxPts = 10
# Output: 1.00000
# Explanation: Alice gets a single card, then stops.
# Example 2:
#
# Input: n = 6, k = 1, maxPts = 10
# Output: 0.60000
# Explanation: Alice gets a single card, then stops.
# In 6 out of 10 possibilities, she is at or below 6 points.
# Example 3:
#
# Input: n = 21, k = 17, maxPts = 10
# Output: 0.73278
#
#
# Constraints:
#
# 0 <= k <= n <= 104
# 1 <= maxPts <= 104
from typing import List


# start time :15:26

def solution(n: int, k: int, maxPts: int) -> float:
     # sliding window is k
     # n is the target
     # range is [1,maxPts]
     # result = []
     # 1 2 3 4 5 6 7 8 9 10

     cards = [x for x in range(1, maxPts+1)]

     result = []

     def back_track(taken: List[int], cards: List[int], totalPts: int):
         if totalPts >= k:
             result.append(totalPts)
             return

         for i in range(len(cards)):
             taken.append(cards[i])
             totalPts += cards[i]
             back_track(taken, cards[:i] + cards[i + 1:], totalPts)
             taken.pop(-1)
             totalPts -= cards[i]


     back_track([], cards, 0)

     win = [x for x in result if x <= n]

     print(f"len(win):{len(win)}, len(total):{len(result)}")
     return len(win)/len(result)



def test_case1():
    result = solution(n=10, k=1, maxPts=10)
    print(result)
    assert result == 1.00000


def test_case2():
    result = solution(n=6, k=1, maxPts=10)
    print(result)
    assert result == 0.60000


def test_case3():
    result = solution(n=21, k=17, maxPts=10)
    print(result)
    assert result == 0.73278


if __name__ == "__main__":
    # test_case1()
    # test_case2()
    test_case3()

