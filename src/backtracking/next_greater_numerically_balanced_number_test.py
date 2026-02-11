import pytest
from next_greater_numerically_balanced_number import solution

@pytest.mark.parametrize("n, expected", [
    (1, 22),
    (1000, 1333),
    (3000, 3133)
])
def test_case(n, expected):
    assert solution(n) == expected