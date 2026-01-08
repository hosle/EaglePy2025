from frequency_of_the_most_frequent_element import solution
import pytest


@pytest.mark.parametrize("nums, k, expected", [
    ([1,2,4], 5, 3),
    ([1,4,8,13], 5, 2),
    ([3,9,6], 2, 1)
])
def test_case(nums, k, expected):
    assert solution(nums, k) == expected


# def test_case1():
#     nums = [1,2,4]
#     result = solution(nums, 5)
#     print(result)
#     assert result == 3

# def test_case2():
#     nums = [1,4,8,13]
#     result = solution(nums, 5)
#     print(result)
#     assert result == 2

# def test_case3():
#     nums = [3,9,6]
#     result = solution(nums, 2)
#     print(result)
#     assert result == 1
