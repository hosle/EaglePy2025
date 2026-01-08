from find_peak_element import solution
import pytest


@pytest.mark.parametrize("nums, expected", [
    ([1,2,3,1], 2),
    ([1,2,1,3,5,6,4], 5),
    ([1,2,3], 2),
    ([4,3,2,1], 0),
    ([4], 0),
    ([1,2,1,3,2], 1)
])
def test_case(nums, expected):
    assert solution(nums) == expected


# def test_case1():
#     assert solution([1,2,3,1]) == 2


# def test_case2():
#     assert solution([1,2,1,3,5,6,4]) == 5

# def test_case3():
#     assert solution([1,2,3]) == 2

# def test_case4():
#     assert solution([4,3,2,1]) == 0

# def test_case5():
#     assert solution([4]) == 0

# def test_case6():
#     assert solution([1,2,1,3,2]) == 1
