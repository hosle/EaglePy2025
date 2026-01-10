import pytest
from meeting_room_ii import solution
from meeting_room_ii import solution2

@pytest.mark.parametrize("intervals, expected", [
    ([[0,30],[5,10],[15,20]], 2),
    ([[7,10],[2,4]], 1)
])
def test_case(intervals, expected):
    assert solution(intervals) == expected
    
@pytest.mark.parametrize("intervals, expected", [
    ([[0,30],[5,10],[15,20]], 2),
    ([[7,10],[2,4]], 1)
])
def test_case2(intervals, expected):
    assert solution2(intervals) == expected