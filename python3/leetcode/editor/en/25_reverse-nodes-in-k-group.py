# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional

from python3.tools.tools import *


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # compute length of the list
        dummy = ListNode(next=head)
        n = 0
        # cnt = head
        while head:
            head = head.next
            n += 1

        p0 = dummy
        while n - k >= 0:
            pre, cur = reverseNode(p0.next, k)
            x = p0.next
            p0.next.next = cur
            p0.next = pre
            p0 = x
            n -= k

        return dummy.next


def reverseNode(node, k):
    pre, cur = None, node
    for _ in range(k):
        nxt = cur.next
        cur.next = pre
        pre = cur
        cur = nxt
    return pre, cur


if __name__ == '__main__':
    s = Solution()
    print_link_node(s.reverseKGroup(to_link_node([1, 2, 3, 4, 5]), 2))
    print_link_node(s.reverseKGroup(to_link_node([1, 2, 3, 4, 5]), 3))
