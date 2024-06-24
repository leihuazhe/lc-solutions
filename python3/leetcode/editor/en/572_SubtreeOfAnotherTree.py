#!/usr/bin/python3
# -*- coding: UTF-8 -*-

# source:  https://leetcode-cn.com/problems/subtree-of-another-tree
# source:  https://leetcode.com/problems/subtree-of-another-tree

# [572]-subtree-of-another-tree

"""
Given the roots of two binary trees root and subRoot, return true if there is a 
subtree of root with the same structure and node values of subRoot and false 
otherwise. 

 A subtree of a binary tree tree is a tree that consists of a node in tree and 
all of this node's descendants. The tree tree could also be considered as a 
subtree of itself. 

 
 Example 1: 
 
 
Input: root = [3,4,5,1,2], subRoot = [4,1,2]
Output: true
 

 Example 2: 
 
 
Input: root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2]
Output: false
 

 
 Constraints: 

 
 The number of nodes in the root tree is in the range [1, 2000]. 
 The number of nodes in the subRoot tree is in the range [1, 1000]. 
 -10⁴ <= root.val <= 10⁴ 
 -10⁴ <= subRoot.val <= 10⁴ 
 

 Related Topics Tree Depth-First Search String Matching Binary Tree Hash 
Function 👍 8161 👎 507

"""
from typing import Optional

from python3.tools.tools import TreeNode


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        flag = self.isSame(root, subRoot)
        if flag:
            return True
        if root:
            # return self.isSame(root.left, subRoot) or self.isSame(root.right, subRoot)
            # 注意这里是递归调用
            return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        return False

    def isSame(self, p: Optional[TreeNode], q: Optional[TreeNode]):
        if p is None or q is None:
            return p is q
        return p.val == q.val and self.isSame(p.left, q.left) and self.isSame(p.right, q.right)


# leetcode submit region end(Prohibit modification and deletion)

"""
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # like same tree, but further.
        flag = self.isSame(root,subRoot)
        if flag:
            return True
        if root:
            return self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)
        return False
    
    def isSame(self,p: Optional[TreeNode], q: Optional[TreeNode]):
        if p is None or q is None:
            return p is q
        return p.val == q.val and self.isSame(p.left,q.left) and self.isSame(p.right,q.right)

"""
