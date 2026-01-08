import pytest
from fruits_into_baskets_iii import solution

@pytest.mark.parametrize("fruits, baskets, expected", [
    ([4,2,5], [3,5,4], 1),
    ([3,6,1], [6,4,7], 0),
    ([1,3,3], [1,2,6], 1),
    ([20,8], [79,4], 1)
])
def test_case(fruits, baskets, expected):
    assert solution(fruits, baskets) == expected

# def test_case():
#     assert solution([4,2,5], [3,5,4]) == 1
#     assert solution([3,6,1], [6,4,7]) == 1
#     assert solution([1,3,3], [1,2,6]) == 1
#     assert solution([20,8], [79,4]) == 1