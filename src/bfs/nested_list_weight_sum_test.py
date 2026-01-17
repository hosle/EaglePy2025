import pytest
from nested_list_weight_sum import solution

@pytest.mark.parametrize("nestedList, expected", [
    ([[1,1],2,[1,1]], 10),
    ([1,[4,[6]]], 27)
])
def test_case(nestedList, expected):
    assert solution(nestedList) == expected