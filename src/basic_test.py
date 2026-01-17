import pytest
from basic import find_unique_number_in_array

@pytest.mark.parametrize("arr, expected",[
    ([2,3,3,5,5], 2),
    ([5,10,8,18,8,10,5],18)
])
def test_case(arr, expected):
    assert find_unique_number_in_array(arr) == expected