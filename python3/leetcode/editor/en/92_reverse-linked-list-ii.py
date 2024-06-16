#!/usr/bin/python3
# -*- coding: UTF-8 -*-
from typing import Optional

from python3.tools.tools import *


# source:  https://leetcode-cn.com/problems/reverse-linked-list-ii
# source:  https://leetcode.com/problems/reverse-linked-list-ii

# [92]-reverse-linked-list-ii

# Given the head of a singly linked list and two integers left and right where 
# left <= right, reverse the nodes of the list from position left to position 
# right, and return the reversed list. 
# 
#  
#  Example 1: 
#  
#  
# Input: head = [1,2,3,4,5], left = 2, right = 4
# Output: [1,4,3,2,5]
#  
# 
#  Example 2: 
# 
#  
# Input: head = [5], left = 1, right = 1
# Output: [5]
#  
# 
#  
#  Constraints: 
# 
#  
#  The number of nodes in the list is n. 
#  1 <= n <= 500 
#  -500 <= Node.val <= 500 
#  1 <= left <= right <= n 
#  
# 
#  
# Follow up: Could you do it in one pass?
# 
#  Related Topics Linked List 👍 11514 👎 610


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.


class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        p0 = dummy
        for _ in range(left - 1):
            p0 = p0.next

        pre, cur = None, p0.next
        for _ in range(right - left + 1):
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt
        p0.next.next = cur
        p0.next = pre

        return dummy.next


# leetcode submit region end(Prohibit modification and deletion)

if __name__ == '__main__':
    s = Solution()
    print_link_node(s.reverseBetween(to_link_node([1, 2, 3, 4, 5, 6, 7]), 2, 5))
