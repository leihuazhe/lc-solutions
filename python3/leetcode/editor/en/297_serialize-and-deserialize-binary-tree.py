#!/usr/bin/python3
# -*- coding: UTF-8 -*-
from collections import defaultdict

from python3.tools.tools import *


# source:  https://leetcode-cn.com/problems/serialize-and-deserialize-binary-tree
# source:  https://leetcode.com/problems/serialize-and-deserialize-binary-tree

# [297]-serialize-and-deserialize-binary-tree

# Serialization is the process of converting a data structure or object into a 
# sequence of bits so that it can be stored in a file or memory buffer, or 
# transmitted across a network connection link to be reconstructed later in the same or 
# another computer environment. 
# 
#  Design an algorithm to serialize and deserialize a binary tree. There is no 
# restriction on how your serialization/deserialization algorithm should work. You 
# just need to ensure that a binary tree can be serialized to a string and this 
# string can be deserialized to the original tree structure. 
# 
#  Clarification: The input/output format is the same as how LeetCode 
# serializes a binary tree. You do not necessarily need to follow this format, so please be 
# creative and come up with different approaches yourself. 
# 
#  
#  Example 1: 
#  
#  
# Input: root = [1,2,3,null,null,4,5]
# Output: [1,2,3,null,null,4,5]
#  
# 
#  Example 2: 
# 
#  
# Input: root = []
# Output: []
#  
# 
#  
#  Constraints: 
# 
#  
#  The number of nodes in the tree is in the range [0, 10⁴]. 
#  -1000 <= Node.val <= 1000 
#  
# 
#  Related Topics String Tree Depth-First Search Breadth-First Search Design 
# Binary Tree 👍 10104 👎 394


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        arr = []
        self.preorder(root, arr)
        pre_str = ','.join([str(i) for i in arr])
        arr.clear()
        self.inorder(root, arr)
        in_str = ','.join([str(i) for i in arr])
        return '|'.join([pre_str, in_str])

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        pre_str, in_str = data.split('|')
        if not pre_str:
            return None
        pre_array = [int(c) for c in list(pre_str.split(','))]
        in_array = [int(c) for c in list(in_str.split(','))]

        inorder_indices = defaultdict(list)
        for i, value in enumerate(in_array):
            inorder_indices[value].append(i)

        def array_to_tree(pre_left, pre_right, in_left, in_right):
            if pre_left > pre_right:
                return None
            # 前序遍历的第一个元素是根节点
            root_val = pre_array[pre_left]
            root = TreeNode(root_val)

            # 获取根节点在中序遍历中的所有位置
            root_inorder_indices = inorder_indices[root_val]

            # 找到符合当前范围的中序索引
            root_inorder_index = None
            for index in root_inorder_indices:
                if in_left <= index <= in_right:
                    root_inorder_index = index
                    root_inorder_indices.remove(index)
                    break
            # 计算左子树的大小
            left_tree_size = root_inorder_index - in_left
            # 递归构建左子树和右子树
            root.left = array_to_tree(pre_left + 1, pre_left + left_tree_size, in_left, root_inorder_index - 1)
            root.right = array_to_tree(pre_left + left_tree_size + 1, pre_right, root_inorder_index + 1, in_right)
            return root

        return array_to_tree(0, len(pre_array) - 1, 0, len(in_array) - 1)

    def preorder(self, root, arr):
        if root is None:
            return
        arr.append(root.val)
        self.preorder(root.left, arr)
        self.preorder(root.right, arr)

    def inorder(self, root, arr):
        if root is None:
            return
        self.inorder(root.left, arr)
        arr.append(root.val)
        self.inorder(root.right, arr)

    # 构建树的递归函数


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
# leetcode submit region end(Prohibit modification and deletion)

if __name__ == '__main__':
    c = Codec()
    tree = to_tree_node([1, 2, 3, None, None, 4, 5])
    data = c.serialize(tree)
    res = c.deserialize(data)
    print(res)
    #     2
    tree = to_tree_node([3, 2, 4, 3])
    data = c.serialize(tree)
    res = c.deserialize(data)
    print(res)
