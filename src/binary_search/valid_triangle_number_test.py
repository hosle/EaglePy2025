from valid_triangle_number import solution
import pytest


@pytest.mark.parametrize("nums, expected", [
    ([2,2,3,4], 3),
    ([4,2,3,4], 4),
    ([0,1,1,1], 1),
    ([0,0,0], 0)
])
def test_case(nums, expected):
    assert solution(nums) == expected


# def test_case1():
#     assert solution([2,2,3,4]) == 3

# def test_case2():
#     assert solution([4,2,3,4]) == 4

# def test_case3():
#     assert solution([0,1,1,1]) == 1

# def test_case4():
#     assert solution([0,0,0]) == 0

