#!/usr/bin/python3
# -*- coding: UTF-8 -*-

# source:  https://leetcode-cn.com/problems/construct-binary-tree-from-preorder-and-postorder-traversal
# source:  https://leetcode.com/problems/construct-binary-tree-from-preorder-and-postorder-traversal

# [889]-construct-binary-tree-from-preorder-and-postorder-traversal

"""
Given two integer arrays, preorder and postorder where preorder is the preorder 
traversal of a binary tree of distinct values and postorder is the postorder 
traversal of the same tree, reconstruct and return the binary tree. 

 If there exist multiple answers, you can return any of them. 

 
 Example 1: 
 
 
Input: preorder = [1,2,4,5,3,6,7], postorder = [4,5,2,6,7,3,1]
Output: [1,2,3,4,5,6,7]
 

 Example 2: 

 
Input: preorder = [1], postorder = [1]
Output: [1]
 

 
 Constraints: 

 
 1 <= preorder.length <= 30 
 1 <= preorder[i] <= preorder.length 
 All the values of preorder are unique. 
 postorder.length == preorder.length 
 1 <= postorder[i] <= postorder.length 
 All the values of postorder are unique. 
 It is guaranteed that preorder and postorder are the preorder traversal and 
postorder traversal of the same binary tree. 
 

 Related Topics Array Hash Table Divide and Conquer Tree Binary Tree 👍 2732 👎 
114

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
    """
    输入：preorder = [1,2,4,5,3,6,7], postorder = [4,5,2,6,7,3,1]
    输出：[1,2,3,4,5,6,7]
    """

    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None
        if len(preorder) > 1:
            left_node = preorder[1]
            left_size = postorder.index(left_node)
            left = self.constructFromPrePost(preorder[1:left_size + 2], postorder[:left_size + 1])
            right = self.constructFromPrePost(preorder[left_size + 2:], postorder[left_size + 1:-1])
            return TreeNode(preorder[0], left, right)
        return TreeNode(preorder[0])


# leetcode submit region end(Prohibit modification and deletion)

if __name__ == '__main__':
    s = Solution()
    print_tree_node(s.constructFromPrePost(preorder=[1, 2, 4, 5, 3, 6, 7], postorder=[4, 5, 2, 6, 7, 3, 1]))
