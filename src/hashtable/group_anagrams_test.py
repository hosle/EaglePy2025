from group_anagrams import solution, compare_nested_sorted
import pytest


def test_case1():
    strs = [""]
    assert solution(strs) == [['']]


def test_case2():
    strs = ['a']
    assert solution(strs) == [['a']]


def test_case3():
    strs = ["eat","tea","tan","ate","nat","bat"]
    assert compare_nested_sorted(solution(strs),[["bat"],["nat","tan"],["ate","eat","tea"]])


# def test_case1():
#     strs = [""]
#     print(solution(strs))
#     assert solution(strs) == [['']]


# def test_case2():
#     strs = ['a']
#
#     assert solution(strs) == [['a']]


# def test_case3():
#     strs = ["eat","tea","tan","ate","nat","bat"]
#     print("result =", solution(strs))
#     assert compare_nested_sorted(solution(strs),[["bat"],["nat","tan"],["ate","eat","tea"]])
