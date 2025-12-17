# https://leetcode.com/problems/all-paths-from-source-to-target/description/
from typing import List


#Given a directed acyclic graph (DAG) of n nodes labeled from 0 to n - 1,
#find all possible paths from node 0 to node n - 1 and return them in any order.
# The graph is given as follows: graph[i] is a list of all nodes you can visit
# from node i (i.e., there is a directed edge from node i to node graph[i][j]).

# Example 1
# Input: graph = [[1,2],[3],[3],[]]
# Output: [[0,1,3],[0,2,3]]
# Explanation: There are two paths: 0 -> 1 -> 3 and 0 -> 2 -> 3.

# Example 2:
# Input: graph = [[4,3,1],[3,2,4],[3],[4],[]]
# Output: [[0,4],[0,3,4],[0,1,3,4],[0,1,2,3,4],[0,1,4]]
#

# Constraints:
#
# n == graph.length
# 2 <= n <= 15
# 0 <= graph[i][j] < n
# graph[i][j] != i (i.e., there will be no self-loops).
# All the elements of graph[i] are unique.
# The input graph is guaranteed to be a DAG.

def solution(ori_graph: List[List[int]]) -> List[List[int]]:
    # [[1,2],[3],[3],[]]
    start = 0
    dest = len(ori_graph) - 1

    result = []

    def traverse(current, path):
        if current == dest:
            result.append(path[:])

        for next_node in ori_graph[current]:
            path.append(next_node)
            traverse(next_node, path)
            path.pop()

    traverse(start, [0])

    return result


def test_1():
    result = solution([[1,2],[3],[3],[]])
    print(result)
    assert result == [[0,1,3],[0,2,3]]


def test_2():
    result = solution([[4,3,1],[3,2,4],[3],[4],[]])
    print(result)
    assert result == [[0,4],[0,3,4],[0,1,3,4],[0,1,2,3,4],[0,1,4]]


if __name__ == '__main__':
    test_1()

    test_2()