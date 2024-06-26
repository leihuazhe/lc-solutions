#!/usr/bin/python3
# -*- coding: UTF-8 -*-

# source:  https://leetcode-cn.com/problems/lowest-common-ancestor-of-deepest-leaves
# source:  https://leetcode.com/problems/lowest-common-ancestor-of-deepest-leaves

# [1123]-lowest-common-ancestor-of-deepest-leaves

"""
Given the root of a binary tree, return the lowest common ancestor of its 
deepest leaves. 

 Recall that: 

 
 The node of a binary tree is a leaf if and only if it has no children 
 The depth of the root of the tree is 0. if the depth of a node is d, the depth 
of each of its children is d + 1. 
 The lowest common ancestor of a set S of nodes, is the node A with the largest 
depth such that every node in S is in the subtree with root A. 
 

 
 Example 1: 
 
 
Input: root = [3,5,1,6,2,0,8,null,null,7,4]
Output: [2,7,4]
Explanation: We return the node with value 2, colored in yellow in the diagram.
The nodes coloured in blue are the deepest leaf-nodes of the tree.
Note that nodes 6, 0, and 8 are also leaf nodes, but the depth of them is 2, 
but the depth of nodes 7 and 4 is 3. 

 Example 2: 

 
Input: root = [1]
Output: [1]
Explanation: The root is the deepest node in the tree, and it's the lca of 
itself.
 

 Example 3: 

 
Input: root = [0,1,3,null,2]
Output: [2]
Explanation: The deepest leaf node in the tree is 2, the lca of one node is 
itself.
 

 
 Constraints: 

 
 The number of nodes in the tree will be in the range [1, 1000]. 
 0 <= Node.val <= 1000 
 The values of the nodes in the tree are unique. 
 

 
 Note: This question is the same as 865: https://leetcode.com/problems/smallest-
subtree-with-all-the-deepest-nodes/ 

 Related Topics Hash Table Tree Depth-First Search Breadth-First Search Binary 
Tree 👍 1958 👎 842

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
class Solution:

    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node) -> (Optional[TreeNode], int):
            if not node:
                return None, 0
            l, ld = dfs(node.left)
            r, rd = dfs(node.right)
            if ld == rd:
                return root, ld
            if ld > rd:
                return dfs(node.left), ld + 1
            if rd > ld:
                return dfs(node.right), rd + 1

        return dfs(root)[0]


# leetcode submit region end(Prohibit modification and deletion)

if __name__ == '__main__':
    array = [1, 2, 3]
    for i in range(0, len(array), 2):
        print(i)
        # print(i + 1)

    # s = Solution()
