#!/usr/bin/python3
# -*- coding: UTF-8 -*-
from typing import Optional

from python3.tools.tools import *


# source:  https://leetcode-cn.com/problems/palindrome-linked-list
# source:  https://leetcode.com/problems/palindrome-linked-list

# [234]-palindrome-linked-list

# Given the head of a singly linked list, return true if it is a palindrome or
# false otherwise.
#
#
#  Example 1:
#
#
# Input: head = [1,2,2,1]
# Output: true
#
#
#  Example 2:
#
#
# Input: head = [1,2]
# Output: false
#
#
#
#  Constraints:
#
#
#  The number of nodes in the list is in the range [1, 10⁵].
#  0 <= Node.val <= 9
#
#
#
# Follow up: Could you do it in
# O(n) time and
# O(1) space?
#
#  Related Topics Linked List Two Pointers Stack Recursion 👍 16388 👎 878


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        mid = self.findMid(head)
        head2 = self.reverseNode(mid)

        while head2:
            if head.val != head2.val:
                return False
            head = head.next
            head2 = head2.next

        return True

    def findMid(self, head: Optional[ListNode]):
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def reverseNode(self, head: Optional[ListNode]):
        pre, cur = None, head
        while cur:
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt
        return pre

        # leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    s = Solution()
    print(s.isPalindrome(to_link_node([1, 2, 2, 1])))
    print(s.isPalindrome(to_link_node([1, 2])))
    print(s.isPalindrome(to_link_node([1, 2, 1])))
