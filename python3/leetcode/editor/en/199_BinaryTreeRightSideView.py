#!/usr/bin/python3
# -*- coding: UTF-8 -*-

# source:  https://leetcode-cn.com/problems/binary-tree-right-side-view
# source:  https://leetcode.com/problems/binary-tree-right-side-view

# [199]-binary-tree-right-side-view

"""
Given the root of a binary tree, imagine yourself standing on the right side of 
it, return the values of the nodes you can see ordered from top to bottom. 

 
 Example 1: 
 
 
Input: root = [1,2,3,null,5,null,4]
Output: [1,3,4]
 

 Example 2: 

 
Input: root = [1,null,3]
Output: [1,3]
 

 Example 3: 

 
Input: root = []
Output: []
 

 
 Constraints: 

 
 The number of nodes in the tree is in the range [0, 100]. 
 -100 <= Node.val <= 100 
 

 Related Topics Tree Depth-First Search Breadth-First Search Binary Tree 👍 1185
4 👎 936

"""
from collections import defaultdict, deque
from typing import List, Optional


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.val)


class Solution:
    """
    可优化选项:
        a.直接在 BFS 中生成结果列表 res，而不是使用 container 来存储所有节点的值。
        b.只在每个深度首次遇到节点时将其值加入 res。
        c.保持了相同的时间复杂度 O(N)，但空间复杂度有所减少，避免了使用 container 的额外空间。
    """

    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        queue = deque()
        queue.append((root, 0))
        max_depth = -1
        res = []
        while queue:
            (cur, depth) = queue.popleft()
            if depth > max_depth:
                max_depth = depth
                res.append(cur.val)

            if cur.right:
                queue.append((cur.right, depth + 1))
            if cur.left:
                queue.append((cur.left, depth + 1))
        return res

    def rightSideViewOne(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        queue = deque()
        container = defaultdict(list)
        queue.append((root, 0))
        while queue:
            (cur, depth) = queue.popleft()
            container[depth].append(cur.val)
            if cur.left:
                queue.append((cur.left, depth + 1))
            if cur.right:
                queue.append((cur.right, depth + 1))

        res = []
        index = 0
        while True:
            if index in container:
                res.append(container[index][-1])
                index += 1
            else:
                break
        return res


# leetcode submit region end(Prohibit modification and deletion)

if __name__ == '__main__':
    s = Solution()
    print(s.rightSideView([]))
    print(s.rightSideView(TreeNode(1, TreeNode(2, TreeNode(5)), TreeNode(3, TreeNode(4)))))
