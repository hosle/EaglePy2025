import pytest
from taking_maximum_energy_from_the_mystic_dungeon import solution

@pytest.mark.parametrize("energy, k, expected", [
    ([5,2,-10,-5,1], 3, 3),
    ([-2,-3,-1], 2, -1),
    ([-1], 0, -1),
    ([1], 0, 1)
])
def test_case(energy, k, expected):
    assert solution(energy, k) == expected