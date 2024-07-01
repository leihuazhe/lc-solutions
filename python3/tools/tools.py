from collections import deque
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


# TreeNode
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.val)


def to_tree_node(data, index=0):
    node = None
    if index < len(data):
        if data[index] == None:
            return
        node = TreeNode(data[index])
        node.left = to_tree_node(data, 2 * index + 1)  # [1, 3, 7, 15, ...]
        node.right = to_tree_node(data, 2 * index + 2)  # [2, 5, 12, 25, ...]
    return node


def print_tree_node(head: TreeNode):
    str_ = ""
    q = deque([head])
    while q:
        size = len(q)
        for _ in range(size):
            cur = q.popleft()
            if cur.left:
                q.append(cur.left)
            if cur.right:
                q.append(cur.right)
            str_ += str(cur.val) + '->'
    print(str_)
