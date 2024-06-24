from math import inf
from typing import Optional

from python3.tools.tools import *

"""
前序遍历: 先访问节点值，再递归左右节点
"""


class PreOrder:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.check(root, -inf, inf)

    def check(self, node, low, up):
        if node is None:
            return True
        if node.val <= low or node.val >= up:
            return False

        return self.check(node.left, low, node.val) and self.check(node.right, node.val, up)


"""
中序遍历: 判断当前节点值是否大于上一个节点值,再记录下来，然后和下一个节点做比较.
"""


class InOrder:
    pre = -inf

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # edge case
        if root is None:
            return True
        # traversal left tree
        if not self.isValidBST(root.left):
            return False
        print(root.val)
        if root.val <= self.pre:
            return False
        # traversal right tree
        return self.isValidBST(root.right)


"""
后序遍历
"""


class PostOrder:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        if not self.isValidBST(root.left):
            return False
        if not self.isValidBST(root.right):
            return False

        l = root.left.val if root.left else -inf
        r = root.right.val if root.right else inf
        print(root.val)
        if root.val <= l or root.val >= r:
            return False

        return True


"""
                5
            2           6
        1       4
            3  
"""

if __name__ == '__main__':
    # in order
    sin = InOrder()
    print(sin.isValidBST(to_tree_node([5, 2, 6, 1, 4, None, None, None, None, 3, None], 0)))
    post = PostOrder()
    print(post.isValidBST(to_tree_node([5, 2, 6, 1, 4, None, None, None, None, 3, None], 0)))
