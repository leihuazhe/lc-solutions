#!/usr/bin/python3
# -*- coding: UTF-8 -*-
from typing import Optional

from python3.tools.tools import ListNode


# source:  https://leetcode-cn.com/problems/reverse-linked-list
# source:  https://leetcode.com/problems/reverse-linked-list

# [206]-reverse-linked-list

# Given the head of a singly linked list, reverse the list, and return the 
# reversed list. 
# 
#  
#  Example 1: 
#  
#  
# Input: head = [1,2,3,4,5]
# Output: [5,4,3,2,1]
#  
# 
#  Example 2: 
#  
#  
# Input: head = [1,2]
# Output: [2,1]
#  
# 
#  Example 3: 
# 
#  
# Input: head = []
# Output: []
#  
# 
#  
#  Constraints: 
# 
#  
#  The number of nodes in the list is the range [0, 5000]. 
#  -5000 <= Node.val <= 5000 
#  
# 
#  
#  Follow up: A linked list can be reversed either iteratively or recursively. 
# Could you implement both? 
# 
#  Related Topics Linked List Recursion 👍 21390 👎 433


# leetcode submit region begin(Prohibit modification and deletion)


def toNode(nums):
    dummy = ListNode()
    cur = dummy
    for n in nums:
        cur.next = ListNode(n)
        cur = cur.next
    return dummy.next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        st = []
        cur = head
        while cur:
            st.append(cur)
            cur = cur.next
        last = st.pop() if st else None
        re_cur = last
        while st:
            x = st.pop()
            re_cur.next = x
            re_cur = x
        if re_cur:
            re_cur.next = None
        return last


# leetcode submit region end(Prohibit modification and deletion)

if __name__ == '__main__':
    s = Solution()
    print(s.reverseList(toNode([1, 2, 3, 4, 5])))
