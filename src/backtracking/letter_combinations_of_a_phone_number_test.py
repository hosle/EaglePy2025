import pytest
from letter_combinations_of_a_phone_number import solution

@pytest.mark.parametrize("digits, expected", [
    ("23", ["ad","ae","af","bd","be","bf","cd","ce","cf"]),
    ("2", ["a", "b", "c"])
])
def test_case(digits, expected):
    assert sorted(solution(digits)) == sorted(expected)