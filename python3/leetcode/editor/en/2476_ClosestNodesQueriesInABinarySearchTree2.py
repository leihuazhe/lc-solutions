# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional

from python3.tools.tools import *


class Solution:
    def closestNodes(self, root: Optional[TreeNode], queries: List[int]) -> List[List[int]]:
        nums = []
        self.toList(root, nums)
        return [self.binary_search(nums, q) for q in queries]

    def toList(self, root, res):
        if root is None:
            return
        self.toList(root.left, res)
        res.append(root.val)
        self.toList(root.right, res)

    def binary_search(self, nums, target):
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] == target:
                return [nums[mid], nums[mid]]
            if nums[mid] < target:  # red
                l = mid + 1
            else:
                r = mid - 1
        if l == len(nums):
            return [nums[-1], -1]
        if r == -1:
            return [-1, nums[0]]
        return [nums[l - 1], nums[l]]


if __name__ == '__main__':
    s = Solution()
    print(s.closestNodes(to_tree_node([6, 2, 13, 1, 4, 9, 15, None, None, None, None, None, None, 14]), [2, 5, 16]))
