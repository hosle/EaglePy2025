from new_21_game import solution
import pytest


@pytest.mark.parametrize("n, k, maxPts, expected", [
    (10, 1, 10, 1.00000),
    (6, 1, 10, 0.60000),
    (21, 17, 10, 0.73278)
])
def test_case(n, k, maxPts, expected):
    assert solution(n, k, maxPts) == expected


# def test_case1():
#     result = solution(n=10, k=1, maxPts=10)
#     print(result)
#     assert result == 1.00000


# def test_case2():
#     result = solution(n=6, k=1, maxPts=10)
#     print(result)
#     assert result == 0.60000


# def test_case3():
#     result = solution(n=21, k=17, maxPts=10)
#     print(result)
#     assert result == 0.73278
