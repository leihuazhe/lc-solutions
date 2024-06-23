#!/usr/bin/python3
# -*- coding: UTF-8 -*-
from typing import Optional

from python3.tools.tools import *


# source:  https://leetcode-cn.com/problems/balanced-binary-tree
# source:  https://leetcode.com/problems/balanced-binary-tree

# [110]-balanced-binary-tree

# Given a binary tree, determine if it is height-balanced. 
# 
#  
#  Example 1: 
#  
#  
# Input: root = [3,9,20,null,null,15,7]
# Output: true
#  
# 
#  Example 2: 
#  
#  
# Input: root = [1,2,2,3,3,null,null,4,4]
# Output: false
#  
# 
#  Example 3: 
# 
#  
# Input: root = []
# Output: true
#  
# 
#  
#  Constraints: 
# 
#  
#  The number of nodes in the tree is in the range [0, 5000]. 
#  -10⁴ <= Node.val <= 10⁴ 
#  
# 
#  Related Topics Tree Depth-First Search Binary Tree 👍 10624 👎 683


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.get_height(root) != -1

    def get_height(self, node: Optional[TreeNode]):
        if node is None:
            return 0
        left_height = self.get_height(node.left)
        if left_height == -1:
            return -1
        right_height = self.get_height(node.right)
        if right_height == -1 or abs(left_height - right_height) > 1:
            return -1
        return max(left_height, right_height) + 1


# leetcode submit region end(Prohibit modification and deletion)

if __name__ == '__main__':
    s = Solution()
    print(s.isBalanced(to_tree_node([3, 9, 20, None, None, 15, 7], 0)))
    print(s.isBalanced(to_tree_node([1, 2, 2, 3, 3, None, None, 4, 4], 0)))
