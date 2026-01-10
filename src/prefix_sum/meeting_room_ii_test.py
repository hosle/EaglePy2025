import pytest
from meeting_room_ii import solution

@pytest.mark.parametrize("intervals, expected", [
    ([[0,30],[5,10],[15,20]], 2),
    ([[7,10],[2,4]], 1)
])
def test_case(intervals, expected):
    assert solution(intervals) == expected