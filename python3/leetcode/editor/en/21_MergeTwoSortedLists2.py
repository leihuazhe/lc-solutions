#!/usr/bin/python3
# -*- coding: UTF-8 -*-

# source:  https://leetcode-cn.com/problems/merge-two-sorted-lists
# source:  https://leetcode.com/problems/merge-two-sorted-lists

# [21]-merge-two-sorted-lists

"""
You are given the heads of two sorted linked lists list1 and list2. 

 Merge the two lists into one sorted list. The list should be made by splicing 
together the nodes of the first two lists. 

 Return the head of the merged linked list. 

 
 Example 1: 
 
 
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
 

 Example 2: 

 
Input: list1 = [], list2 = []
Output: []
 

 Example 3: 

 
Input: list1 = [], list2 = [0]
Output: [0]
 

 
 Constraints: 

 
 The number of nodes in both lists is in the range [0, 50]. 
 -100 <= Node.val <= 100 
 Both list1 and list2 are sorted in non-decreasing order. 
 

 Related Topics Linked List Recursion 👍 21655 👎 2108

"""
from typing import Optional

from python3.tools.tools import *


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2
        if list2 is None:
            return list1

        if list1.val < list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2


# leetcode submit region end(Prohibit modification and deletion)

# <= timestamp
def findTarget(nums, timestamp):
    nums.sort()
    l, r = 0, len(nums) - 1
    while l <= r:
        mid = l + (r - l) // 2
        if nums[mid] > timestamp:
            r = mid - 1
        else:
            l = mid + 1
    return r


if __name__ == '__main__':
    x = {}
    x1 = [x.keys()]
    print(findTarget([1, 2, 3, 4, 6, 7, 8, 9, 10], 5))

    # Input: list1 = [1,2,4], list2 = [1,3,4]
    # Output: [1,1,2,3,4,4]
    l1 = to_link_node([1, 2, 4])
    l2 = to_link_node([1, 3, 4])
    s = Solution()
    print_link_node(s.mergeTwoLists(l1, l2))
