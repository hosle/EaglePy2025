import pytest
from random_pick_with_weight2 import Solution


@pytest.mark.parametrize(
    "command, param, expected",
    [
        (
            [
                "Solution",
                "pickIndex",
                "pickIndex",
                "pickIndex",
                "pickIndex",
                "pickIndex",
            ],
            [[[1, 3]], [], [], [], [], []],
            [None, 1, 1, 1, 1, 0],
        ),
        (
            ["Solution","pickIndex"],
            [[[1]],[]],
            [None,0]),
    ],
)
def test_case(command, param, expected):
    solution = None
    result = []
    
    for i in range (len(command)):
        match command[i]:
            case "Solution":
                solution = Solution(param[i][0])
            case "pickIndex":
                result.append(solution.pickIndex())
            case _:
                continue
    
    assert result == expected[1:]
        
