#!/usr/bin/python3
# -*- coding: UTF-8 -*-

# source:  https://leetcode-cn.com/problems/minimum-absolute-difference-in-bst
# source:  https://leetcode.com/problems/minimum-absolute-difference-in-bst

# [530]-minimum-absolute-difference-in-bst

"""
Given the root of a Binary Search Tree (BST), return the minimum absolute 
difference between the values of any two different nodes in the tree. 

 
 Example 1: 
 
 
Input: root = [4,2,6,1,3]
Output: 1
 

 Example 2: 
 
 
Input: root = [1,0,48,null,null,12,49]
Output: 1
 

 
 Constraints: 

 
 The number of nodes in the tree is in the range [2, 10⁴]. 
 0 <= Node.val <= 10⁵ 
 

 
 Note: This question is the same as 783: https://leetcode.com/problems/minimum-
distance-between-bst-nodes/ 

 Related Topics Tree Depth-First Search Breadth-First Search Binary Search Tree 
Binary Tree 👍 4363 👎 222

"""
from math import inf
from typing import Optional

from python3.tools.tools import *


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    pre = -inf
    ans = inf

    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        # in order
        def get_min_abs(node):
            if node is None:
                return
            get_min_abs(node.left)
            x = node.val
            self.ans = min(self.ans, abs(self.pre - x))
            self.pre = x
            get_min_abs(node.right)

        get_min_abs(root)

        return self.ans

    # leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    s = Solution()
    print(s.getMinimumDifference(to_tree_node([4, 2, 6, 1, 3])))
