#!/usr/bin/python3
# -*- coding: UTF-8 -*-

# source:  https://leetcode-cn.com/problems/range-sum-of-bst
# source:  https://leetcode.com/problems/range-sum-of-bst

# [938]-range-sum-of-bst

"""
Given the root node of a binary search tree and two integers low and high, 
return the sum of values of all nodes with a value in the inclusive range [low, high]
. 

 
 Example 1: 
 
 
Input: root = [10,5,15,3,7,null,18], low = 7, high = 15
Output: 32
Explanation: Nodes 7, 10, and 15 are in the range [7, 15]. 7 + 10 + 15 = 32.
 

 Example 2: 
 
 
Input: root = [10,5,15,3,7,13,18,1,null,6], low = 6, high = 10
Output: 23
Explanation: Nodes 6, 7, and 10 are in the range [6, 10]. 6 + 7 + 10 = 23.
 

 
 Constraints: 

 
 The number of nodes in the tree is in the range [1, 2 * 10⁴]. 
 1 <= Node.val <= 10⁵ 
 1 <= low <= high <= 10⁵ 
 All Node.val are unique. 
 

 Related Topics Tree Depth-First Search Binary Search Tree Binary Tree 👍 6921 ?
? 377

"""
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
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        ans = []
        self.find_nums(root, low, high, ans)
        return sum(ans)

    def find_nums(self, node, low, high, res):
        if node is None:
            return
        if node.val >= low and node.val <= high:
            res.append(node.val)
        self.find_nums(node.left, low, high, res)
        self.find_nums(node.right, low, high, res)


# leetcode submit region end(Prohibit modification and deletion)

if __name__ == '__main__':
    s = Solution()
    print(s.rangeSumBST(to_tree_node([10, 5, 15, 3, 7, None, 18]), 7, 15))
    print(s.rangeSumBST(to_tree_node([10, 5, 15, 3, 7, 13, 18, 1, None, 6]), 6, 10))
