from find_right_interval import solution
import pytest


@pytest.mark.parametrize("intervals, expected", [
    ([[1, 2]], [-1]),
    ([[3,4],[2,3],[1,2]], [-1,0,1]),
    ([[1, 4], [2, 3], [3, 4]], [-1,2,-1]),
    ([[1,12],[2,9],[3,10],[13,14],[15,16],[16,17]], [3,3,3,4,5,-1]),
    ([[1,1],[3,4]], [0,-1])
])
def test_case(intervals, expected):
    assert solution(intervals) == expected


# def test_case_1():
#     intervals = [[1, 2]]
#     assert solution(intervals) == [-1]


# def test_case_2():
#     intervals = [[3,4],[2,3],[1,2]]
#     assert solution(intervals) == [-1,0,1]


# def test_case_3():
#     intervals = [[1, 4], [2, 3], [3, 4]]
#     assert solution(intervals) == [-1,2,-1]

# def test_case_4():
#     intervals = [[1,12],[2,9],[3,10],[13,14],[15,16],[16,17]]
#     assert solution(intervals) == [3,3,3,4,5,-1]

# def test_case_5():
#     intervals = [[1,1],[3,4]]
#     assert solution(intervals) == [0,-1]
