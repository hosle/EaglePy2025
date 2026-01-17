import pytest
from find_the_student_that_will_replace_the_chalk import solution

@pytest.mark.parametrize("chalk, k, expected",[
    ([5,1,5], 22, 0),
    ([3,4,1,2], 25, 1)
])
def test_case(chalk, k, expected):
    assert solution(chalk, k) == expected