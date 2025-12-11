from typing import List


def solution(array) -> List[int]:

    result = []

    def find_permutation(collect:List[int], remain:List[int]):

        if len(remain) == 0:
            result.append(collect[:])

        for i in range(len(remain)):
            collect.append(remain[i])

            find_permutation(collect, remain[:i] + remain[i+1:])

            collect.pop()

    find_permutation([], array)

    return result

def testcase1():
    array = [1,2,3,4]

    print(solution(array))


if __name__ == "__main__":
    testcase1()