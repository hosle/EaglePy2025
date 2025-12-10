def solution(ori_input:list)-> list:
    result = []

    def backtrack(result_item:list, input:list):
        if len(input) == 0:
            result.append(result_item)
            return

        for item in input:
            # result_item.append(item)
            next_input = input.copy()
            next_input.remove(item)

            backtrack(result_item + [item], next_input)


    backtrack([], ori_input)

    return result


if __name__ == "__main__":
    ori = [1,2,3]

    print(ori)

    print(solution(ori))