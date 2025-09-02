from typing import List


def quick_sort(input: List[int]) -> List[int]:

    if len(input) <= 1:
        return input

    mid = partition(input)

    left_sorted = quick_sort(input[0:mid])

    right_sorted = quick_sort(input[mid:])

    left_sorted.extend(right_sorted)

    return left_sorted


def partition(input: List[int]) -> int:
    small_count = 0

    for i in range(len(input) - 1) :
        if input[i] <= input[-1]:
            input[i], input[small_count] =  input[small_count], input[i]
            small_count += 1

    input[small_count], input[-1] = input[-1], input[small_count]

    return small_count



if __name__ == "__main__":
    print("This is quick sort")

    input = [3,2,1,5,7,12,44,32]

    print(f"input : {input}")

    result = quick_sort(input)

    print(f"sorted : {result}")


    input2 = [0,1,2,3,4,5,6]

    print(f"input1 = {input2[1:4]}")