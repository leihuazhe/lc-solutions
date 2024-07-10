#!/usr/bin/python3
# -*- coding: UTF-8 -*-

# source:  https://leetcode-cn.com/problems/house-robber-iii
# source:  https://leetcode.com/problems/house-robber-iii

# [337]-house-robber-iii

"""
The thief has found himself a new place for his thievery again. There is only 
one entrance to this area, called root. 

 Besides the root, each house has one and only one parent house. After a tour, 
the smart thief realized that all houses in this place form a binary tree. It 
will automatically contact the police if two directly-linked houses were broken 
into on the same night. 

 Given the root of the binary tree, return the maximum amount of money the 
thief can rob without alerting the police. 

 
 Example 1: 
 
 
Input: root = [3,2,3,null,3,null,1]
Output: 7
Explanation: Maximum amount of money the thief can rob = 3 + 3 + 1 = 7.
 

 Example 2: 
 
 
Input: root = [3,4,5,1,3,null,1]
Output: 9
Explanation: Maximum amount of money the thief can rob = 4 + 5 = 9.
 

 
 Constraints: 

 
 The number of nodes in the tree is in the range [1, 10⁴]. 
 0 <= Node.val <= 10⁴ 
 

 Related Topics Dynamic Programming Tree Depth-First Search Binary Tree 👍 8509 
👎 143

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
    def rob(self, root: Optional[TreeNode]) -> int:
        ans = 0
        q = deque()
        q.append(root)
        st = []
        while q:
            size = len(q)
            total = 0
            for _ in range(size):
                node = q.popleft()
                total += node.val
                if node.left:
                    q.append(node.left)
                if node.rigth:
                    q.append(node.right)
            st.append(total)
        # 正常计算
        n = len(st)
        dp = [0] * n
        dp[0] = st[0]
        dp[1] = max(st[0], st[1])
        for i in range(n):
            dp[i] = max(dp[i - 1], dp[i - 2] + st[i])
        return dp[n - 1]




# leetcode submit region end(Prohibit modification and deletion)
