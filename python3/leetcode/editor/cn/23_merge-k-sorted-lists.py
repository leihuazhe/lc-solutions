#!/usr/bin/python3
# -*- coding: UTF-8 -*-
import heapq
from typing import Optional, List


# source:  https://leetcode-cn.com/problems/merge-k-sorted-lists
# source:  https://leetcode.com/problems/merge-k-sorted-lists

# [23]-merge-k-sorted-lists

# 给你一个链表数组，每个链表都已经按升序排列。 
# 
#  请你将所有链表合并到一个升序链表中，返回合并后的链表。 
# 
#  
# 
#  示例 1： 
# 
#  输入：lists = [[1,4,5],[1,3,4],[2,6]]
# 输出：[1,1,2,3,4,4,5,6]
# 解释：链表数组如下：
# [
#   1->4->5,
#   1->3->4,
#   2->6
# ]
# 将它们合并到一个有序链表中得到。
# 1->1->2->3->4->4->5->6
#  
# 
#  示例 2： 
# 
#  输入：lists = []
# 输出：[]
#  
# 
#  示例 3： 
# 
#  输入：lists = [[]]
# 输出：[]
#  
# 
#  
# 
#  提示： 
# 
#  
#  k == lists.length 
#  0 <= k <= 10^4 
#  0 <= lists[i].length <= 500 
#  -10^4 <= lists[i][j] <= 10^4 
#  lists[i] 按 升序 排列 
#  lists[i].length 的总和不超过 10^4 
#  
# 
#  Related Topics 链表 分治 堆（优先队列） 归并排序 👍 2819 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        res = []
        while self:
            res.append(self.val)
            self = self.next
        return str(res)


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode()
        cur = dummy
        min_heap = []

        def extract(i: int, node: ListNode):
            while node and i > 0:
                node = node.next
                i -= 1
            return node.val

        def has_next(i: int, node: ListNode):
            while node and i > 0:
                node = node.next
                i -= 1
            return node.next is not None

        for i, array in enumerate(lists):
            # value, list_index, element_index
            if array:
                heapq.heappush(min_heap, (extract(0, array), i, 0))

        while min_heap:
            value, list_index, element_index = heapq.heappop(min_heap)
            cur.next = ListNode(value)
            cur = cur.next
            if has_next(element_index, lists[list_index]):
                heapq.heappush(min_heap, (extract(element_index + 1, lists[list_index]), list_index, element_index + 1))

        return dummy.next


# leetcode submit region end(Prohibit modification and deletion)

def buildList(nums: List[int]) -> ListNode:
    head = ListNode(nums[0])
    node = head
    for num in nums[1:]:
        node.next = ListNode(num)
        node = node.next
    return head


if __name__ == '__main__':
    solution = Solution()
    print(solution.mergeKLists([buildList([1, 4, 5]), buildList([1, 3, 4]), buildList([2, 6])]))
