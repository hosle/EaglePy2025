# https://leetcode.com/problems/path-sum-ii/description/
# Given the root of a binary tree and an integer targetSum,
# return all root-to-leaf paths where the sum of the node values in the path equals targetSum.
# Each path should be returned as a list of the node values, not node references.
#
# A root-to-leaf path is a path starting from the root and ending at any leaf node.
# A leaf is a node with no children.

# Example 1
# Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
# Output: [[5,4,11,2],[5,8,4,5]]
# Explanation: There are two paths whose sum equals targetSum:
# 5 + 4 + 11 + 2 = 22
# 5 + 8 + 4 + 5 = 22

# Example 2
# Input: root = [1,2,3], targetSum = 5
# Output: []

# Example 3
# Input: root = [1,2], targetSum = 0
# Output: []

# Constraints:
#
# The number of nodes in the tree is in the range [0, 5000].
# -1000 <= Node.val <= 1000
# -1000 <= targetSum <= 1000

from typing import Optional

class Node:
    def __init__(self, val, left: Optional['Node']=None, right: Optional['Node'] = None):
        self.val = val
        self.left = left
        self.right = right


def construct_tree(tree_arr: list) -> Node:
    root = None
    queue = []
    if len(tree_arr) > 0:
        root = Node(tree_arr[0])
        queue = [root]

    for i in range(1, len(tree_arr), 2):
        head = queue.pop(0)
        print(f"head from queue:{head.val}, i={i}")

        if tree_arr[i] is not None:
            head.left = Node(tree_arr[i])
            queue.append(head.left)

        if i+1 < len(tree_arr) and tree_arr[i+1] is not None:
            head.right = Node(tree_arr[i+1])
            queue.append(head.right)

    return root


def solution(tree_root:Node, target_sum:int)-> list:
    result = []
    def traverse(root:Node, path:list, sum:int):
        if root is None:
            return False

        path.append(root.val)
        new_sum = sum + root.val

        # # Approach 1: append/pop - More efficient
        # path.append(val)      # O(1) - adds to end
        # backtrack(path[:])    # O(n) - copies only when needed (at leaf)
        # path.pop()            # O(1) - removes from end
        #
        # # Approach 2: concatenation - Less efficient
        # backtrack(path + [val])  # O(n) - creates new list EVERY recursive call

        if not root.left and not root.right:
            if new_sum == target_sum:
                # result.append(path[:])   # Appends a COPY of path
                # result.append(path)      # Appends a REFERENCE to path
                result.append(path[:])

        traverse(root.left, path, new_sum)

        traverse(root.right, path, new_sum)

        path.pop()


    traverse(tree_root, [], 0)

    return result


def test_case1():
    tree_arr = [5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1]

    targetSum = 22

    tree_root = construct_tree(tree_arr)

    result = solution(tree_root, targetSum)

    print(result)

    assert result == [[5, 4, 11, 2], [5, 8, 4, 5]]

def test_case2():
    case2 = [1, 2, 3]

    targetSum = 5

    assert solution(construct_tree(case2), targetSum) == []

def test_case3():
    case3 = [1, 2]

    targetSum3 = 0

    assert solution(construct_tree(case3), targetSum3) == []

def test_case4():
    case4 = [1, 2]

    targetSum4 = 1

    tree = construct_tree(case4)

    result = solution(tree, targetSum4)

    print(result)

    assert result == []

def test_case5():
    case5 = [-2, None, -3]
    targetSum5 = -5
    tree = construct_tree(case5)
    result = solution(tree, targetSum5)
    assert result == [[-2, -3]]

if __name__ == "__main__":
    test_case1()
    test_case2()
    test_case3()
    test_case4()
    test_case5()








