#!/usr/bin/python3
# -*- coding: UTF-8 -*-

# source:  https://leetcode-cn.com/problems/closest-nodes-queries-in-a-binary-search-tree
# source:  https://leetcode.com/problems/closest-nodes-queries-in-a-binary-search-tree

# [2476]-closest-nodes-queries-in-a-binary-search-tree

"""
You are given the root of a binary search tree and an array queries of size n 
consisting of positive integers. 

 Find a 2D array answer of size n where answer[i] = [mini, maxi]: 

 
 mini is the largest value in the tree that is smaller than or equal to queries[
i]. If a such value does not exist, add -1 instead. 
 maxi is the smallest value in the tree that is greater than or equal to 
queries[i]. If a such value does not exist, add -1 instead. 
 

 Return the array answer. 

 
 Example 1: 
 
 
Input: root = [6,2,13,1,4,9,15,null,null,null,null,null,null,14], queries = [2,5
,16]
Output: [[2,2],[4,6],[15,-1]]
Explanation: We answer the queries in the following way:
- The largest number that is smaller or equal than 2 in the tree is 2, and the 
smallest number that is greater or equal than 2 is still 2. So the answer for 
the first query is [2,2].
- The largest number that is smaller or equal than 5 in the tree is 4, and the 
smallest number that is greater or equal than 5 is 6. So the answer for the 
second query is [4,6].
- The largest number that is smaller or equal than 16 in the tree is 15, and 
the smallest number that is greater or equal than 16 does not exist. So the answer 
for the third query is [15,-1].
 

 Example 2: 
 
 
Input: root = [4,null,9], queries = [3]
Output: [[-1,4]]
Explanation: The largest number that is smaller or equal to 3 in the tree does 
not exist, and the smallest number that is greater or equal to 3 is 4. So the 
answer for the query is [-1,4].
 

 
 Constraints: 

 
 The number of nodes in the tree is in the range [2, 10⁵]. 
 1 <= Node.val <= 10⁶ 
 n == queries.length 
 1 <= n <= 10⁵ 
 1 <= queries[i] <= 10⁶ 
 

 Related Topics Array Binary Search Tree Depth-First Search Binary Search Tree 
Binary Tree 👍 431 👎 115

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
    def closestNodes(self, root: Optional[TreeNode], queries: List[int]) -> List[List[int]]:
        # [2,5,16]
        ans = []
        for q in queries:
            res = [-1, -1]
            self.find_closest(root, q, res)
            ans.append(res[:])

        return ans

    def find_closest(self, node: Optional[TreeNode], target, res: List[int]):
        if node is None:
            return
        x = node.val
        if x == target:
            res[0], res[1] = x, x
        else:
            if res[0] != -1:
                res[0] = x if target > x > res[0] else res[0]
            else:
                res[0] = x if target > x else res[0]
            if res[1] != -1:
                res[1] = x if target < x < res[1] else res[1]
            else:
                res[1] = x if target < x else res[1]

            # left
        self.find_closest(node.left, target, res)
        # right
        self.find_closest(node.right, target, res)


# leetcode submit region end(Prohibit modification and deletion)

if __name__ == '__main__':
    s = Solution()
    print(s.closestNodes(to_tree_node([6, 2, 13, 1, 4, 9, 15, None, None, None, None, None, None, 14]), [2, 5, 16]))
