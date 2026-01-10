import pytest
from maximum_frequency_of_an_element_after_performing_operations_i_2 import solution

@pytest.mark.parametrize("nums, k, number_operations, expected", [
    ([5,11,20,20], 5, 1, 2),
    ([1,4,5], 1, 2, 2),
    ([2,49],97,0, 1),
    ([18,57],97,2,2),
    ([88,53],27,2,2),
    ([1,90], 76, 1, 1),
    ([2,70,73],39,2,2)
])
def test_case(nums, k, number_operations, expected):
    assert solution(nums, k, number_operations) == expected