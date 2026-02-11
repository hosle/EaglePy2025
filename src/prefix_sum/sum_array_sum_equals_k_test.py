import pytest
from sum_array_sum_equals_k import solution
from sum_array_sum_equals_k import solution2
from sum_array_sum_equals_k import solution3

@pytest.mark.parametrize("numbers, k, expected", [
    ([1,1,1], 2, 2),
    ([1,2,3], 3, 2),
    ([1], 0, 0),
    ([1], 1, 1),
    ([-1,-1, 1], 0, 1),
    ([1,1,1], 1, 3)
])
def test_case(numbers, k, expected):
    assert solution(numbers, k) == expected
    

@pytest.mark.parametrize("numbers, k, expected", [
    ([1,1,1], 2, 2),
    ([1,2,3], 3, 2),
    ([1], 0, 0),
    ([1], 1, 1),
    ([-1,-1, 1], 0, 1),
    ([1,1,1], 1, 3)
])
def test_case2(numbers, k, expected):
    assert solution2(numbers, k) == expected
    
    
@pytest.mark.parametrize("numbers, k, expected", [
    ([1,1,1], 2, 2),
    ([1,2,3], 3, 2)
    # ([1], 0, 0),
    # ([1], 1, 1),
    # ([-1,-1, 1], 0, 1),
    # ([1,1,1], 1, 3)
])
def test_case3(numbers, k, expected):
    assert solution3(numbers, k) == expected