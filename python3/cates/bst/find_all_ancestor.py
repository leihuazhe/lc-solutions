from typing import Optional

from python3.tools.tools import *


class Solution:

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


if __name__ == '__main__':
    s = Solution()
    res = s.find_ancestors(to_tree_node([1, 2, 3, 4, 5, None, None, 7]), 7)
    print(res)
    print(s.find_ancestors(to_tree_node([1, 2, 3, 4, 5, None, None, 7]), 3))
