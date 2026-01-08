from longest_continuous_subarray_with_absolute_diff import solution
import pytest


@pytest.mark.parametrize("nums, limit, expected", [
    ([8,2,4,7], 4, 2),
    ([10,1,2,4,7,2], 5, 4),
    ([4,2,2,2,4,4,2,2], 0, 3)
])
def test_case(nums, limit, expected):
    assert solution(nums, limit) == expected


# def test_case1():
#     result = solution([8,2,4,7], 4)
#     print(result)
#     assert result == 2


# def test_case2():
#     result = solution([10,1,2,4,7,2], 5)
#     print(result)
#     assert result == 4


# def test_case3():
#     result = solution([4,2,2,2,4,4,2,2], 0)
#     print(result)
#     assert result == 3
