#!/usr/bin/python3
# -*- coding: UTF-8 -*-

# source:  https://leetcode-cn.com/problems/validate-binary-search-tree
# source:  https://leetcode.com/problems/validate-binary-search-tree

# [98]-validate-binary-search-tree

"""
Given the root of a binary tree, determine if it is a valid binary search tree (
BST). 

 A valid BST is defined as follows: 

 
 The left subtree of a node contains only nodes with keys less than the node's 
key. 
 The right subtree of a node contains only nodes with keys greater than the 
node's key. 
 Both the left and right subtrees must also be binary search trees. 
 

 
 Example 1: 
 
 
Input: root = [2,1,3]
Output: true
 

 Example 2: 
 
 
Input: root = [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.
 

 
 Constraints: 

 
 The number of nodes in the tree is in the range [1, 10⁴]. 
 -2³¹ <= Node.val <= 2³¹ - 1 
 

 Related Topics Tree Depth-First Search Binary Search Tree Binary Tree 👍 16671 
👎 1362

"""
from cmath import inf
from typing import Optional


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def dfs(node: Optional[TreeNode], lower: int, upper: int):
            if not node:
                return True
            if node.val <= lower or node.val >= upper:
                return False
            return dfs(node.left, lower, node.val) and dfs(node.right, node.val, upper)

        return dfs(root, -inf, inf)


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    s = Solution()
    print(s.isValidBST(root=TreeNode(val=2, left=TreeNode(val=1), right=TreeNode(val=3))))
    print(s.isValidBST(root=
                       TreeNode(val=13,
                                left=TreeNode(10, TreeNode(9), TreeNode(12)),
                                right=TreeNode(15, TreeNode(12), TreeNode(17)),
                                ))
          )
