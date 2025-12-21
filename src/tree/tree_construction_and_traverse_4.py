from collections import deque
from typing import List
from TreeNode import TreeNode

# Took 20 mins to complete
def construct_tree(ori_arr: List[int]) -> TreeNode:
    if not ori_arr:
        return TreeNode(None)

    root = TreeNode(ori_arr[0])

    queue = deque([root])

    i = 1

    while i < len(ori_arr) and queue:
        head = queue.popleft()

        if head:
            left = TreeNode(ori_arr[i])
            head.left = left
            queue.append(left)
        i += 1

        if i < len(ori_arr) and head:
            right = TreeNode(ori_arr[i])
            head.right = right
            queue.append(right)
        i += 1

    return root


def traverse_dfs(root: TreeNode):
    if not root:
        return

    if root.val:
        print(root.val, end=', ')

    traverse_dfs(root.left)
    traverse_dfs(root.right)


def traverse_bfs(root: TreeNode):
    if not root:
        return

    queue = deque([[root]])

    while queue:
        cur_level = queue.popleft()
        next_level = []

        for item in cur_level:
            if not item:
                continue

            print(item.val, end=", ")

            next_level.append(item.left)
            next_level.append(item.right)

        if next_level:
            queue.append(next_level)


def test_case_1():
    tree = construct_tree([3, 4, 5, 6, 7, None, 4, None, 3, None, None, None, None, 8, 9])

    traverse_dfs(tree)

    print("bfs tree")
    traverse_bfs(tree)


if __name__ == '__main__':
    test_case_1()


