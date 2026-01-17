import pytest
from number_of_islands import solution


@pytest.mark.parametrize(
    "grid, expected",
    [
        (
            [
                ["1", "1", "1", "1", "0"],
                ["1", "1", "0", "1", "0"],
                ["1", "1", "0", "0", "0"],
                ["0", "0", "0", "0", "0"],
            ],
            1,
        ),
        (
            [
                ["1", "1", "0", "0", "0"],
                ["1", "1", "0", "0", "0"],
                ["0", "0", "1", "0", "0"],
                ["0", "0", "0", "1", "1"],
            ],
            3,
        ),
        ([["1", "1", "1"], ["0", "1", "0"], ["0", "1", "0"]],
        1)
    ]
)
def test_case(grid, expected):
    assert solution(grid) == expected
