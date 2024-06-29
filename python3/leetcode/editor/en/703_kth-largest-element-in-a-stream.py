#!/usr/bin/python3
# -*- coding: UTF-8 -*-
from heapq import heappush, heappop
from typing import List


# source:  https://leetcode-cn.com/problems/kth-largest-element-in-a-stream
# source:  https://leetcode.com/problems/kth-largest-element-in-a-stream

# [703]-kth-largest-element-in-a-stream

# Design a class to find the kᵗʰ largest element in a stream. Note that it is 
# the kᵗʰ largest element in the sorted order, not the kᵗʰ distinct element. 
# 
#  Implement KthLargest class: 
# 
#  
#  KthLargest(int k, int[] nums) Initializes the object with the integer k and 
# the stream of integers nums. 
#  int add(int val) Appends the integer val to the stream and returns the 
# element representing the kᵗʰ largest element in the stream. 
#  
# 
#  
#  Example 1: 
# 
#  
# Input
# ["KthLargest", "add", "add", "add", "add", "add"]
# [[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]]
# Output
# [null, 4, 5, 5, 8, 8]
# 
# Explanation
# KthLargest kthLargest = new KthLargest(3, [4, 5, 8, 2]);
# kthLargest.add(3);   // return 4
# kthLargest.add(5);   // return 5
# kthLargest.add(10);  // return 5
# kthLargest.add(9);   // return 8
# kthLargest.add(4);   // return 8
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= k <= 10⁴ 
#  0 <= nums.length <= 10⁴ 
#  -10⁴ <= nums[i] <= 10⁴ 
#  -10⁴ <= val <= 10⁴ 
#  At most 10⁴ calls will be made to add. 
#  It is guaranteed that there will be at least k elements in the array when 
# you search for the kᵗʰ element. 
#  
# 
#  Related Topics Tree Design Binary Search Tree Heap (Priority Queue) Binary 
# Tree Data Stream 👍 5436 👎 3500


# leetcode submit region begin(Prohibit modification and deletion)
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums
        self.st = []
        for n in self.nums:
            heappush(self.st, n)

        while len(self.st) > k:
            heappop(self.st)

    def add(self, val: int) -> int:
        self.nums.append(val)
        heappush(self.st, val)
        heappop(self.st)
        return self.st[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
# leetcode submit region end(Prohibit modification and deletion)

if __name__ == '__main__':
    k = 3
    nums = [4, 5, 8, 2]
    kthLargest = KthLargest(k, nums)
    print(kthLargest.add(3))  # return 4
    print(kthLargest.add(5))  # return 5
    print(kthLargest.add(10))  # return 5
    print(kthLargest.add(9))  # return 8
    print(kthLargest.add(4))  # return 8
