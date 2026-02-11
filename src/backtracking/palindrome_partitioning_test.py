import pytest
from palindrome_partitioning import solution
from palindrome_partitioning import solution2

@pytest.mark.parametrize("s, expected", [
    ("aab", [["a","a","b"],["aa","b"]]),
    ("a", [["a"]])
])
def test_case(s, expected):
    assert solution(s) == expected
    
    
@pytest.mark.parametrize("s, expected", [
    ("aab", [["a","a","b"],["aa","b"]]),
    ("a", [["a"]])
])
def test_case2(s, expected):
    assert solution2(s) == expected