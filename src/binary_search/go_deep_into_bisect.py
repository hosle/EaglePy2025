import bisect
from typing import List

def test_case():
    input_list = [1, 3, 3, 3, 5]

    print(">> search exact : ")
    print(binary_search_exact(input_list, 3))

    print(">> search lower bound : ")
    print(binary_search_lower_bound(input_list, 3))

    print(">> search upper bound : ")
    print(binary_search_upper_bound(input_list, 3))


    print(">> python built-in function bisect")
    print(bisect.bisect(input_list,3))

    print(">> python built-in function bisect_left")
    print(bisect.bisect_left(input_list,3))

    print(">> python built-in function bisect_right")
    print(bisect.bisect_right(input_list, 3))


def binary_search_exact(arr:List[int], target: int):
    low = 0
    high = len(arr) - 1

    while low < high:
        mid = low + (high - low) // 2

        if arr[mid] == target:
            low = mid + 1
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid

    return low


# search range is [lower, upper)
def binary_search_lower_bound(arr:List[int], target: int):
    low = 0
    high = len(arr) - 1

    while low < high:
        mid = low + (high - low) // 2

        if arr[mid] < target:
            low = mid + 1
        else:
            high = mid

    return low


# search range is (lower, upper]
def binary_search_upper_bound(arr: List[int], target: int):
    low = 0
    high = len(arr) - 1

    while low < high:
        mid = low + (high - low) // 2

        if arr[mid] <= target:
            low = mid + 1
        else:
            high = mid

    return low




if __name__ == '__main__':
    test_case()