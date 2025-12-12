
class TreeNode2:
    def __init__(self, val: int, left: 'TreeNode2 | None' = None, right: 'TreeNode2 | None' = None):
        self.val = val
        self.left = left
        self.right = right


def construction_tree() -> TreeNode2:

    ori_arr = [9, None, 21, None, None, 3, 4, None, None, None,None,2, None, 8, 11]

    root = TreeNode2(ori_arr[0])

    queue = [root]

    i = 1

    while queue and i < len(ori_arr):
        head = queue.pop(0)

        if ori_arr[i] and head:
            left_node = TreeNode2(ori_arr[i])
            head.left = left_node
            queue.append(left_node)
        else:
            queue.append(None)
        i += 1

        if i < len(ori_arr):
            if ori_arr[i] is not None:
                right_node = TreeNode2(ori_arr[i])
                head.right = right_node
                queue.append(right_node)
            else:
                queue.append(None)
        i += 1

    return root


def travers_dfs(root: TreeNode2):
    if not root:
        return

    print(root.val, end=",")

    travers_dfs(root.left)

    travers_dfs(root.right)


def test_case1():
    tree_root1 = construction_tree()

    travers_dfs(tree_root1)

if __name__ == "__main__":
    test_case1()







