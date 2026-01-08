from path_sum import solution, construct_tree
import pytest


def test_case1():
    tree_arr = [5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1]
    targetSum = 22
    tree_root = construct_tree(tree_arr)
    result = solution(tree_root, targetSum)
    assert result == [[5, 4, 11, 2], [5, 8, 4, 5]]

def test_case2():
    case2 = [1, 2, 3]
    targetSum = 5
    assert solution(construct_tree(case2), targetSum) == []

def test_case3():
    case3 = [1, 2]
    targetSum3 = 0
    assert solution(construct_tree(case3), targetSum3) == []

def test_case4():
    case4 = [1, 2]
    targetSum4 = 1
    tree = construct_tree(case4)
    result = solution(tree, targetSum4)
    assert result == []

def test_case5():
    case5 = [-2, None, -3]
    targetSum5 = -5
    tree = construct_tree(case5)
    result = solution(tree, targetSum5)
    assert result == [[-2, -3]]


# def test_case1():
#     tree_arr = [5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1]
#
#     targetSum = 22
#
#     tree_root = construct_tree(tree_arr)
#
#     result = solution(tree_root, targetSum)
#
#     print(result)
#
#     assert result == [[5, 4, 11, 2], [5, 8, 4, 5]]

# def test_case2():
#     case2 = [1, 2, 3]
#
#     targetSum = 5
#
#     assert solution(construct_tree(case2), targetSum) == []

# def test_case3():
#     case3 = [1, 2]
#
#     targetSum3 = 0
#
#     assert solution(construct_tree(case3), targetSum3) == []

# def test_case4():
#     case4 = [1, 2]
#
#     targetSum4 = 1
#
#     tree = construct_tree(case4)
#
#     result = solution(tree, targetSum4)
#
#     print(result)
#
#     assert result == []

# def test_case5():
#     case5 = [-2, None, -3]
#     targetSum5 = -5
#     tree = construct_tree(case5)
#     result = solution(tree, targetSum5)
#     assert result == [[-2, -3]]
