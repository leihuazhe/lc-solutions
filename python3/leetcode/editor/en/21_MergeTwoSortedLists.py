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
        # sorted linked lists list1 and list2.
        cur = dummy = ListNode()
        while list1 and list2:
            if list1.val <= list2.val:
                cur.next = ListNode(list1.val)
                list1 = list1.next
            else:
                cur.next = ListNode(list2.val)
                list2 = list2.next
            # TODO 容易遗忘的
            cur = cur.next

        cur.next = list1 if list1 else list2
        return dummy.next


# leetcode submit region end(Prohibit modification and deletion)

if __name__ == '__main__':
    # Input: list1 = [1,2,4], list2 = [1,3,4]
    # Output: [1,1,2,3,4,4]
    l1 = to_link_node([1, 2, 4])
    l2 = to_link_node([1, 3, 4])
    s = Solution()
    print_link_node(s.mergeTwoLists(l1, l2))
