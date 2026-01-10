import pytest
from brightest_position_on_street import solution

@pytest.mark.parametrize("lights, expected", [
    ([[-3,2],[1,2],[3,3]], -1),
    ([[1,0],[0,1]], 1),
    ([[1,2]], -1),
    ([[-4,4],[1,0],[-5,0],[-2,1],[3,4]], -1),
    ([[1,2],[-4,1],[4,5]],-1)
])
def test_case(lights, expected):
    assert solution(lights) == expected