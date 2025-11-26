# a list of warehouse, value represent the each warehouse capacity
# [8, 20, 15,9]

# question : input task list as [100, 20, 30], each value represent the task amount,
# traverse the warehouse to process the task, if capacity full, move to next one.
# if final warehouse is fulfilled, move back to the first warehouse.
# if task value is -1, means to take a break for the warehouse.

# output the warehouse number that the last to process the task list.

def solution(warehouse:list, tasks:list) -> list:

    f_result = []
    end_id = 0

    for item in tasks:
        if item == -1:
            end_id = 0
            continue

        end_id = find_last_warehouse_id(item, warehouse, end_id)

        f_result.append(end_id)

    return f_result


def find_last_warehouse_id(amount, wh, start_id) -> int:
    accumulated = wh[start_id]
    warehouse_size = len(wh)
    i = start_id

    while accumulated < amount:
        i = (i + 1) % warehouse_size
        accumulated += wh[i]

    return i


if __name__ == "__main__":
    warehouse = [8, 20, 15, 9]
    task = [100, 2, 20, 30]
    result = solution(warehouse, task)

    print(result)

    task2 = [100, -1, 2, 20, 30]
    result2 = solution(warehouse, task2)

    print(result2)
