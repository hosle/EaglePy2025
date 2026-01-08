from partition_array_into_disjoint_intervals import solution
import pytest


@pytest.mark.parametrize("nums, expected", [
    ([5,0,3,8,6], 3),
    ([1,1,1,0,6,12], 4)
])
def test_case(nums, expected):
    assert solution(nums) == expected


# def test_case1():
#     nums = [5,0,3,8,6]
#     assert solution(nums) == 3


# def test_case2():
#     nums = [1,1,1,0,6,12]
#     assert solution(nums) == 4
