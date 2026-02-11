import pytest
from bit_operation import solution
from bit_operation import solution2
import time

@pytest.mark.parametrize("s, expected", [
    ("111", 5),
    ("11011",8),
    ("100100",7)
])
def test_case(s, expected):
    assert solution(s) == expected
    
def test_case():
    
    s_arr = ["1" for x in range(400000)]
    s = "".join(s_arr)
    
    time_start = time.time()
    solution(s)
    time_spent = time.time() - time_start
    
    print(f"Solution time cost : {time_spent}")

    time_start2 = time.time()
    solution2(s)
    time_spent2 = time.time() - time_start2
    
    print(f"Solution2 time cost : {time_spent2}")
    