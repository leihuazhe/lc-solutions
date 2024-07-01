#!/usr/bin/python3
# -*- coding: UTF-8 -*-

# source:  https://leetcode-cn.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal
# source:  https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal

# [106]-construct-binary-tree-from-inorder-and-postorder-traversal

"""
Given two integer arrays inorder and postorder where inorder is the inorder 
traversal of a binary tree and postorder is the postorder traversal of the same 
tree, construct and return the binary tree. 

 
 Example 1: 
 
 
Input: inorder = [9,3,15,20,7], postorder = [9,15,7,20,3]
Output: [3,9,20,null,null,15,7]
 

 Example 2: 

 
Input: inorder = [-1], postorder = [-1]
Output: [-1]
 

 
 Constraints: 

 
 1 <= inorder.length <= 3000 
 postorder.length == inorder.length 
 -3000 <= inorder[i], postorder[i] <= 3000 
 inorder and postorder consist of unique values. 
 Each value of postorder also appears in inorder. 
 inorder is guaranteed to be the inorder traversal of the tree. 
 postorder is guaranteed to be the postorder traversal of the tree. 
 

 Related Topics Array Hash Table Divide and Conquer Tree Binary Tree 👍 7969 👎 
130

"""
from typing import List, Optional

from python3.tools.tools import TreeNode


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
    #     if not postorder:
    #         return None
    #     left_size = inorder.index(postorder[-1])
    #     left = self.buildTree(inorder[:left_size], postorder[:left_size])
    #     right = self.buildTree(inorder[left_size + 1:], postorder[left_size:-1])
    #     return TreeNode(postorder[-1], left, right)
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        index = {val: i for i, val in enumerate(inorder)}

        # [ ) open intervals.
        def dfs(in_l, in_r, post_l, post_r):
            if post_l == post_r:
                return None
            left_size = index[postorder[post_r - 1]] - in_l
            left = dfs(in_l, in_l + left_size, post_l, post_l + left_size)
            right = dfs(in_l + left_size + 1, in_r, post_l + left_size, post_r - 1)
            return TreeNode(postorder[post_r - 1], left, right)

        return dfs(0, len(inorder), 0, len(postorder))


# leetcode submit region end(Prohibit modification and deletion)

if __name__ == '__main__':
    s = Solution()
    print(s.buildTree(inorder=[9, 3, 15, 20, 7], postorder=[9, 15, 7, 20, 3]))
    print(s.buildTree(inorder=[-1], postorder=[-1]))
