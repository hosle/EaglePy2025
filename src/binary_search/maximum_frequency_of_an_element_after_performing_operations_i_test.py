from maximum_frequency_of_an_element_after_performing_operations_i import solution
import pytest


@pytest.mark.parametrize("nums, k, numOperations, expected", [
    ([1,4,5], 1, 2, 2),
    ([5,11,20,20], 5, 1, 2),
    ([5], 7, 0, 1),
    ([2, 49], 97, 0, 1)
])
def test_case(nums, k, numOperations, expected):
    assert solution(nums, k, numOperations) == expected


# def test_case1():
#     result = solution([1,4,5], 1,2)
#     print(result)
#     assert result == 2


# def test_case2():
#     result = solution([5,11,20,20], 5, 1)
#     print(result)
#     assert result == 2

# def test_case3():
#     result = solution([5], 7, 0)
#     print(result)
#     assert result == 1

# def test_case4():
#     result = solution([2, 49], 97, 0)
#     print(result)
#     assert result == 1
