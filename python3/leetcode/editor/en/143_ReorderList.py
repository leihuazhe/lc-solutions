#!/usr/bin/python3
# -*- coding: UTF-8 -*-

# source:  https://leetcode-cn.com/problems/reorder-list
# source:  https://leetcode.com/problems/reorder-list

# [143]-reorder-list

"""
You are given the head of a singly linked-list. The list can be represented as: 


 
L0 → L1 → … → Ln - 1 → Ln
 

 Reorder the list to be on the following form: 

 
L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
 

 You may not modify the values in the list's nodes. Only nodes themselves may 
be changed. 

 
 Example 1: 
 
 
Input: head = [1,2,3,4]
Output: [1,4,2,3]
 

 Example 2: 
 
 
Input: head = [1,2,3,4,5]
Output: [1,5,2,4,3]
 

 
 Constraints: 

 
 The number of nodes in the list is in the range [1, 5 * 10⁴]. 
 1 <= Node.val <= 1000 
 

 Related Topics Linked List Two Pointers Stack Recursion 👍 11022 👎 402

"""
import copy
from typing import Optional

from python3.tools.tools import *


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        cur = copy.deepcopy(head)
        reversedHead, count = reverseList(cur)
        cur = head
        flag = True
        while count > 0:
            if flag % 2 == 0:
                cur.next = reversedHead
                reversedHead = reversedHead.next
            else:
                cur.next = head
                head = head.next
            cur = cur.next
            count -= 1

        print_link_node(head)


def reverseList(head):
    n = 0
    pre, cur = None, head
    while cur:
        nxt = cur.next
        cur.next = pre
        pre = cur
        cur = nxt
        n += 1
    return pre, n


# leetcode submit region end(Prohibit modification and deletion)

if __name__ == '__main__':
    s = Solution()
    nodeList = to_link_node([1, 2, 3, 4])
    s.reorderList(nodeList)
