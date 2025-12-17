
class GraphNode:
    def __init__(self, weight: int):
        self.weight = weight
        self.nextNode = list()


def graph_construction() -> dict:

    ori_arr = [("A", "B", 1), ("B", "C", 2), ("C", "D", 3), ("A", "E", 4), ("B", "E", 5), ("E", "D", 6)]

    graph_dir = dict[str, list]()

    for start, end, weight in ori_arr:
        new_list = graph_dir.get(start, [])
        new_list.append((end, weight))
        graph_dir[start] = new_list

    return graph_dir


#traverse graph, print all paths and sum up its weight
def traverse_graph():
    ori_graph = {'A': [('B', 1), ('E', 4)], 'B': [('C', 2), ('E', 5)], 'C': [('D', 3)], 'E': [('D', 6)]}

    result = []

    start = "A"

    end = "D"

    def traverse(head, path, sum_weight):

        if head == end:
            result.append((path[:], sum_weight))
            return

        for next_name, weight in ori_graph[head]:

            path.append(next_name)

            sum_weight += weight

            traverse(next_name, path, sum_weight)

            path.pop()

            sum_weight -= weight

    traverse(start, [start], 0)

    print(result)



def test_case_1():
    graph_directory = graph_construction()

    traverse_graph()

if __name__ == "__main__":
    test_case_1()
