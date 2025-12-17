from collections import deque
from typing import List
from TreeNode import TreeNode

# 9, 20, 7, 4, none, none, 8, none, none, none, none, none, none, none, 2



def construct_tree(ori_list: List[int]) -> 'TreeNode|None' :
    if not ori_list:
        return None

    root = TreeNode(ori_list[0])

    queue = deque([root])

    i = 1

    while queue and i < len(ori_list):
        head = queue.popleft()

        if head:
            left = TreeNode(ori_list[i])
            head.left = left
            queue.append(left)
        else:
            queue.append(None)

        i += 1

        if i < len(ori_list):
            if head:
                right = TreeNode(ori_list[i])
                head.right = right
                queue.append(right)
            else:
                queue.append(None)

        i += 1

    return root


def traverse_dfs(root: TreeNode):
    if not root:
        return

    print(root.val, end=", ")

    traverse_dfs(root.left)

    traverse_dfs(root.right)


def traverse_bfs(root: TreeNode, total_level: int):
    if not root:
        return

    queue = deque([[root]])

    count = 0

    while queue:
        level = queue.popleft()

        next_level = []
        count += 1

        for node in level:
            if node:
                print(node.val, end=", ")

                next_level.append(node.left)
                next_level.append(node.right)
            else:
                print("None", end=", ")

        if next_level and count <= total_level:
            queue.append(next_level)


def test_case_1():
    ori_list = [9, 20, 7, 4, None, None, 8, None, None, None, None, None, None, None, 2]

    root = construct_tree(ori_list)

    traverse_dfs(root)

    print()

    traverse_bfs(root, 3)


if __name__ == '__main__':
    test_case_1()