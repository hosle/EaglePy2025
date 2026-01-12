from arabic_to_roman import solution
import pytest

@pytest.mark.parametrize("numbers, expected", [
    (1994, "MCMXCIV"),
    (58, "LVIII"),
    (3749, "MMMDCCXLIX")
])
def test_case(numbers, expected):
    assert solution(numbers) == expected