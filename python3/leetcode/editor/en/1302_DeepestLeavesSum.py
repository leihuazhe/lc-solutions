#!/usr/bin/python3
# -*- coding: UTF-8 -*-

# source:  https://leetcode-cn.com/problems/deepest-leaves-sum
# source:  https://leetcode.com/problems/deepest-leaves-sum

# [1302]-deepest-leaves-sum

"""
Given the root of a binary tree, return the sum of values of its deepest leaves.


 
 Example 1: 
 
 
Input: root = [1,2,3,4,5,null,6,7,null,null,null,null,8]
Output: 15
 

 Example 2: 

 
Input: root = [6,7,8,2,7,1,3,9,null,1,4,null,null,null,5]
Output: 19
 

 
 Constraints: 

 
 The number of nodes in the tree is in the range [1, 10⁴]. 
 1 <= Node.val <= 100 
 

 Related Topics Tree Depth-First Search Breadth-First Search Binary Tree 👍 4686
 👎 123

"""
from collections import deque
from typing import Optional

from python3.tools.tools import TreeNode


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        q = deque()
        q.append((root, 0))
        max_depth = 0
        ans = 0
        while q:
            node, cur_depth = q.popleft()
            if max_depth < cur_depth:
                ans = node.val
            elif max_depth == cur_depth:
                ans += node.val

            if node.left:
                q.append((node.left, cur_depth + 1))
            if node.right:
                q.append((node.right, cur_depth + 1))

        return ans

    # leetcode submit region end(Prohibit modification and deletion)
