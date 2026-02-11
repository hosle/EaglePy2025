import pytest
from generate_parentheses import solution

@pytest.mark.parametrize("n, expected", [
    (3, ["((()))","(()())","(())()","()(())","()()()"]),
    (1, ["()"]),
])
def test_case(n, expected):
    assert solution(n) == expected