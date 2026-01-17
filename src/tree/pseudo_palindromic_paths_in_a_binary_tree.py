# https://leetcode.com/problems/pseudo-palindromic-paths-in-a-binary-tree/
# Given a binary tree where node values are digits from 1 to 9. A path in the binary tree is said to be pseudo-palindromic if at least one permutation of the node values in the path is a palindrome.
# Return the number of pseudo-palindromic paths going from the root node to leaf nodes.

 

# Example 1:
#      2
#.    /. \
#.   3.   1
#. /  \.   \
#. 3. 1.    1
# Input: root = [2,3,1,3,1,null,1]
# Output: 2 
# Explanation: The figure above represents the given binary tree. There are three paths going from the root node to leaf nodes: the red path [2,3,3], the green path [2,1,1], and the path [2,3,1]. Among these paths only red path and green path are pseudo-palindromic paths since the red path [2,3,3] can be rearranged in [3,2,3] (palindrome) and the green path [2,1,1] can be rearranged in [1,2,1] (palindrome).
# Example 2:
#
#.      2
#.    /.  \
#.   1.    1
#.  / \
#  1  3
#      \
#.      1    
# Input: root = [2,1,1,1,3,null,null,null,null,null,1]
# Output: 1 
# Explanation: The figure above represents the given binary tree. There are three paths going from the root node to leaf nodes: the green path [2,1,1], the path [2,1,3,1], and the path [2,1]. Among these paths only the green path is pseudo-palindromic since [2,1,1] can be rearranged in [1,2,1] (palindrome).
# Example 3:

# Input: root = [9]
# Output: 1

import TreeNode
from typing import Optional
from typing import List

def solution2(root: Optional[TreeNode]) -> int:
    count = 0
        
    stack = [(root, 0) ]
    while stack:
        node, path = stack.pop()
        if node is not None:
            # compute occurences of each digit 
            # in the corresponding register
            path = path ^ (1 << node.val)
            # if it's a leaf, check if the path is pseudo-palindromic
            if node.left is None and node.right is None:
                # check if at most one digit has an odd frequency
                if path & (path - 1) == 0:
                    count += 1
            else:
                stack.append((node.right, path))
                stack.append((node.left, path))
    
    return count

def solution(root: Optional[TreeNode]) -> int:
    
    count_arr = {}
    result = 0
    
    def traverse(root: Optional[TreeNode]):
        nonlocal result
        nonlocal count_arr

        if not root:
            return

        count_arr[root.val] = count_arr.get(root.val, 0) + 1
        # count_arr.add(root.val)

        if root.left == None and root.right == None:
            print(f"{count_arr=}")
            total = 0
            for key,value in count_arr.items():
                if value%2 != 0:
                    total += 1
            
            if total <= 1:
                result += 1

            count_arr[root.val] -= 1
            return
        
        traverse(root.left)
        traverse(root.right)
        count_arr[root.val] -= 1
    
    traverse(root)
    
    return result