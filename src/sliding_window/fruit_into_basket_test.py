from fruit_into_basket import solution
import pytest


@pytest.mark.parametrize("fruits, expected", [
    ([1,2,1], 3),
    ([0,1,2,2], 3),
    ([1,2,3,2,2], 4),
    ([1], 1),
    ([1,2], 2),
    ([1, 1], 2),
    ([1, 2, 1], 3),
    ([1, 2, 3], 2)
])
def test_case(fruits, expected):
    assert solution(fruits) == expected


# def test_case1():
#     result = solution([1,2,1])
#     print(result)
#     assert result == 3


# def test_case2():
#     result = solution([0,1,2,2])
#     print(result)
#     assert result == 3

# def test_case3():
#     result = solution([1,2,3,2,2])
#     print(result)
#     assert result == 4

# def test_case4():
#     result = solution([1])
#     print(result)
#     assert result == 1

# def test_case5():
#     result = solution([1,2])
#     print(result)
#     assert result == 2

# def test_case6():
#     result = solution([1, 1])
#     print(result)
#     assert result == 2

# def test_case7():
#     result = solution([1, 2, 1])
#     print(result)
#     assert result == 3

# def test_case8():
#     result = solution([1, 2, 3])
#     print(result)
#     assert result == 2
