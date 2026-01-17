# https://leetcode.com/problems/binary-tree-vertical-order-traversal/description/
#
#
# Given the root of a binary tree, return the vertical order traversal of its nodes' values. (i.e., from top to bottom, column by column).
#
# If two nodes are in the same row and column, the order should be from left to right.
#
#
# Example 1:
# Input: root = [3,9,20,null,null,15,7]
# Output: [[9],[3,15],[20],[7]]
# Example 2:
# Input: root = [3,9,8,4,0,1,7]
# Output: [[4],[9],[3,0,1],[8],[7]]
# Example 3:
# Input: root = [1,2,3,4,10,9,11,null,5,null,null,null,null,null,null,null,6]
# Output: [[4],[2,5],[1,10,9,6],[3],[11]]
# Constraints:
# The number of nodes in the tree is in the range [0, 100].
# -100 <= Node.val <= 100
#
#
import TreeNode
from typing import List
from typing import Optional
from collections import deque

def verticalOrder(root: Optional[TreeNode]) -> List[List[int]]:

    if not root:
        return []
    
    bfs_queue = [(0, root)]
    
    column_dict = {}
    
    while bfs_queue:
        col, cur_node = bfs_queue.pop(0)
        
        column_elements = column_dict.get(col, [])
        column_elements.append(cur_node.val)
        
        column_dict[col] = column_elements
        
        if cur_node.left:        
            bfs_queue.append((col - 1, cur_node.left))
        
        if cur_node.right:
            bfs_queue.append((col + 1, cur_node.right))
    
    # print(f"{column_dict=}")
    
    sorted_dict = sorted(column_dict.items(), key= lambda item: item[0])
    result = [x[1] for x in sorted_dict]
    # print(f"{result=}")
    return result
    
        
            