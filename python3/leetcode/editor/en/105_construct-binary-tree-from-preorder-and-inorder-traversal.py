#!/usr/bin/python3
# -*- coding: UTF-8 -*-
from typing import List, Optional

from python3.tools.tools import TreeNode


# source:  https://leetcode-cn.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal
# source:  https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal

# [105]-construct-binary-tree-from-preorder-and-inorder-traversal

# Given two integer arrays preorder and inorder where preorder is the preorder 
# traversal of a binary tree and inorder is the inorder traversal of the same tree,
#  construct and return the binary tree. 
# 
#  
#  Example 1: 
#  
#  
# Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
# Output: [3,9,20,null,null,15,7]
#  
# 
#  Example 2: 
# 
#  
# Input: preorder = [-1], inorder = [-1]
# Output: [-1]
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= preorder.length <= 3000 
#  inorder.length == preorder.length 
#  -3000 <= preorder[i], inorder[i] <= 3000 
#  preorder and inorder consist of unique values. 
#  Each value of inorder also appears in preorder. 
#  preorder is guaranteed to be the preorder traversal of the tree. 
#  inorder is guaranteed to be the inorder traversal of the tree. 
#  
# 
#  Related Topics Array Hash Table Divide and Conquer Tree Binary Tree 👍 14871 
# 👎 503


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None
        left_size = inorder.index(preorder[0])
        left = self.buildTree(preorder[1: left_size + 1], inorder[:left_size])
        right = self.buildTree(preorder[left_size + 1:], inorder[left_size + 1:])
        return TreeNode(preorder[0], left, right)

    def find_ancestors(self, root: Optional[TreeNode], target: int):
        if root is None:
            return []
        if root.val == target:
            return [root.val]
        #  return 以后 就是上一层了。当前这一层可以理解为: 4的父节点.
        left = self.find_ancestors(root.left, target)
        if left:
            return [root.val] + left
        right = self.find_ancestors(root.right, target)
        if right:
            return [root.val] + right

    def all_ancestor(self, root: Optional[TreeNode], target):
        ans = []

        def dfs(node):
            if node is None:
                return False
            if node.val == target:
                ans.append(node.val)
                return True
            left = dfs(node.left)
            right = dfs(node.right)

            if left or right:
                ans.append(node.val)
                return True
            
        dfs(root)
        return ans


# leetcode submit region end(Prohibit modification and deletion)

if __name__ == '__main__':
    s = Solution()
    trees = s.buildTree([3, 9, 20, 15, 7], [9, 3, 15, 20, 7])
    print(s.all_ancestor(trees, 15))
    print(s.find_ancestors(trees, 15))
