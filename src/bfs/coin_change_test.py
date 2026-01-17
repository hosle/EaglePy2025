import pytest
from coin_change import solution

@pytest.mark.parametrize("coins, amount, expected", [
    ([1,2,5], 11, 3),
    ([2], 3, -1),
    ([1], 0, 0)
])
def test_case(coins, amount, expected):
    assert solution(coins, amount) == expected