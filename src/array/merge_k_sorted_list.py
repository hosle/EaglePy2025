# merge k sorted list,
# input [[2,30,41],[5,8,16],[6,14,20]]
# output [2,5,6,8,14,16,20,30,41]
import heapq

def solution(input_list) -> list:
    hq = []
    for array in input_list:
        hq.extend(array)

    heapq.heapify(hq)

    result = []

    while hq:
        result.append(heapq.heappop(hq))

    print("sorted result:", result)

    return result

if __name__ == "__main__":
    case1 = [[2,30,41], [5,8,16], [6,14,20]]

    assert solution(case1) == [2,5,6,8,14,16,20,30,41]


