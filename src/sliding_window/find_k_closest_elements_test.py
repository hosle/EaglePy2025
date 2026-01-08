from find_k_closest_elements import solution4
import pytest


@pytest.mark.parametrize("arr, k, x, expected", [
    ([1,2,3,4,5], 4, 3, [1,2,3,4]),
    ([1,1,2,3,4,5], 4, -1, [1, 1, 2, 3]),
    ([1,1,1,10,10,10], 1, 9, [10]),
    ([0,1,1,1,2,3,6,7,8,9], 9, 4, [0,1,1,1,2,3,6,7,8])
])
def test_case(arr, k, x, expected):
    assert solution4(arr, k, x) == expected


# def test_case1():
#     result = solution4([1,2,3,4,5], 4, 3)
#     print(result)
#     assert result == [1,2,3,4]


# def test_case2():
#     result = solution4([1,1,2,3,4,5], 4, -1)
#     print(result)
#     assert result == [1, 1, 2, 3]

# def test_case3():
#     result = solution4([1,1,1,10,10,10], 1, 9)
#     print(result)
#     assert result == [10]

# def test_case4():
#     result = solution4([0,1,1,1,2,3,6,7,8,9], 9, 4)
#     print(result)
#     assert result == [0,1,1,1,2,3,6,7,8]
