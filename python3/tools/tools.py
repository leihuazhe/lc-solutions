from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return str(self.val)


def to_link_node(nums: List[int]) -> ListNode:
    dummy = ListNode()
    cur = dummy
    for n in nums:
        cur.next = ListNode(n)
        cur = cur.next
    return dummy.next


def print_link_node(head: ListNode):
    str_ = ""
    cur = head
    while cur:
        str_ += str(cur.val) + '->'
        cur = cur.next
    print(str_)
