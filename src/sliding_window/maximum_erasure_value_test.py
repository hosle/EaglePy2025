from maximum_erasure_value import solution
import pytest


@pytest.mark.parametrize("nums, expected", [
    ([4,2,4,5,6], 17),
    ([5,2,1,2,5,2,1,2,5], 8),
    ([5], 5),
    ([5, 5], 5),
    ([4,2,4,4,5,6], 15)
])
def test_case(nums, expected):
    assert solution(nums) == expected


# def test_case_1():
#     nums = [4,2,4,5,6]
#     result = solution(nums)
#     print("test 1 : ", result)
#     assert(result == 17)

# def test_case_2():
#     nums = [5,2,1,2,5,2,1,2,5]
#     result = solution(nums)
#     print("test 2 : ", result)
#     assert (result == 8)

# def test_case_3():
#     nums = [5]
#     result = solution(nums)
#     print("test 3 : ", result)
#     assert (result == 5)

# def test_case_4():
#     nums = [5, 5]
#     result = solution(nums)
#     print("test 4 : ", result)
#     assert (result == 5)

# def test_case_5():
#     nums = [4,2,4,4,5,6]
#     result = solution(nums)
#     print("test 5 : ", result)
#     assert(result == 15)
