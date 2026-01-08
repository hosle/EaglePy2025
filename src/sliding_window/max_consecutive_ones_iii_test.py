from max_consecutive_ones_iii import solution
import pytest


@pytest.mark.parametrize("nums, k, expected", [
    ([1,1,1,0,0,0,1,1,1,1,0], 2, 6),
    ([0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], 3, 10),
    ([1], 1, 1),
    ([0], 1, 1),
    ([1], 0, 1),
    ([0], 0, 0)
])
def test_case(nums, k, expected):
    assert solution(nums, k) == expected


# def test_case1():
#     result = solution([1,1,1,0,0,0,1,1,1,1,0], 2)
#     print(result)
#     assert result == 6


# def test_case2():
#     result = solution([0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], 3)
#     print(result)
#     assert result == 10

# def test_case3():
#     result = solution([1], 1)
#     print(result)
#     assert result == 1

# def test_case4():
#     result = solution([0], 1)
#     print(result)
#     assert result == 1


# def test_case5():
#     result = solution([1], 0)
#     print(result)
#     assert result == 1


# def test_case6():
#     result = solution([0], 0)
#     print(result)
#     assert result == 0
