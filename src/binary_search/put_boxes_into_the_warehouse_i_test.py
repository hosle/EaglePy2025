from put_boxes_into_the_warehouse_i import solution
from put_boxes_into_the_warehouse_i import solution2
import pytest


@pytest.mark.parametrize("boxes, warehouse, expected", [
    ([4,3,4,1], [5,3,3,4,1], 3),
    ([1,2,2,3,4], [3,4,1,2], 3),
    ([1,2,3], [1,2,3,4], 1),
    ([4,4,1,1], [5,4,3,3,1], 4),
    ([4,1,8,7], [7,4,2,2,5], 3)
])
def test_case(boxes, warehouse, expected):
    # assert solution(boxes, warehouse) == expected
    assert solution2(boxes, warehouse) == expected