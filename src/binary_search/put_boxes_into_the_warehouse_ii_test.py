from put_boxes_into_the_warehouse_ii import solution
import pytest


@pytest.mark.parametrize("boxes, warehouse, expected", [
    ([1,2,2,3,4], [3,4,1,2], 4),
    ([3,5,5,2], [2,1,3,4,5], 3)
])
def test_case(boxes, warehouse, expected):
    assert solution(boxes, warehouse) == expected