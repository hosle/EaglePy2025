

class TreeNode:
    def __init__(self, val:int, left: 'TreeNode | None' = None, right: 'TreeNode | None' = None):

        # no comma at the end of the line, otherwise , it becomes a tuple
        self.val = val
        self.left = left
        self.right = right


def construct_tree(ori_array) -> TreeNode:

    root = TreeNode(ori_array[0])

    queue = [root]

    for i in range(1, len(ori_array), 2):
        head = queue.pop(0)
        print(f"processing node {head.val}")

        left = TreeNode(ori_array[i])
        head.left = left
        queue.append(left)

        if i+1 < len(ori_array):
            right = TreeNode(ori_array[i+1])
            head.right = right
            queue.append(right)

    return root


def test_case1():
    print("test case 1")

    ori_array = [8, 10, 14, None, 2, 7, 6, None, None, 1, 3, 4, None, None, 5]

    root = construct_tree(ori_array)

    print("- traverse tree dfs: ")

    traverse_tree_dfs(root)

    traverse_tree_bfs(root)

    traverse_tree_zigzag(root)



def test_case2():
    print("test case 2")

    ori_array = [8, 10]

    root = construct_tree(ori_array)

    print("- traverse tree dfs: ")

    traverse_tree_dfs(root)

    traverse_tree_bfs(root)

    traverse_tree_zigzag(root)


def test_case3():
    ori_arr = [9, None, 21, None, None, 3, 4, None, None, None,None,2, None, 8, 11]

    root = construct_tree(ori_arr)

    print("- traverse tree dfs: ")

    traverse_tree_dfs(root)


def traverse_tree_dfs(node: TreeNode):
    if not node: return

    print(node.val, end=",")

    traverse_tree_dfs(node.left)

    traverse_tree_dfs(node.right)


def traverse_tree_bfs(node: TreeNode):

    print("\n- traverse tree bfs")

    queue = [node]

    while queue:
        head = queue.pop(0)

        print(head.val, end=", ")

        if head.left:
            queue.append(head.left)

        if head.right:
            queue.append(head.right)


def traverse_tree_zigzag(node: TreeNode):
    print("\n- traverse tree zigzag")

    queue = [[node]]

    need_reversed = False

    while queue:
        layer = queue.pop(0)

        next_layer = []

        # separate the print and add operation
        if need_reversed:
            layer_to_print = layer[::-1]
        else:
            layer_to_print = layer[:]

        for item_print in layer_to_print:
            print(item_print.val, end=", ")

        print("layer size: " + str(len(layer)))

        need_reversed = not need_reversed

        for item in layer:

            if item.left:
                next_layer.append(item.left)

            if item.right:
                next_layer.append(item.right)

        # important, only append when next layer is contented.

        if next_layer:
            queue.append(next_layer)


if __name__ == "__main__":
    # test_case1()
    # test_case2()
    test_case3()

