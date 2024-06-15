#!/usr/bin/python3
# -*- coding: UTF-8 -*-
from typing import List


# source:  https://leetcode-cn.com/problems/count-the-number-of-fair-pairs
# source:  https://leetcode.com/problems/count-the-number-of-fair-pairs

# [2563]-count-the-number-of-fair-pairs

# Given a 0-indexed integer array nums of size n and two integers lower and 
# upper, return the number of fair pairs. 
# 
#  A pair (i, j) is fair if: 
# 
#  
#  0 <= i < j < n, and 
#  lower <= nums[i] + nums[j] <= upper 
#  
# 
#  
#  Example 1: 
# 
#  
# Input: nums = [0,1,7,4,4,5], lower = 3, upper = 6
# Output: 6
# Explanation: There are 6 fair pairs: (0,3), (0,4), (0,5), (1,3), (1,4), and (1
# ,5).
#  
# 
#  Example 2: 
# 
#  
# Input: nums = [1,7,9,2,5], lower = 11, upper = 11
# Output: 1
# Explanation: There is a single fair pair: (2,3).
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= nums.length <= 10⁵ 
#  nums.length == n 
#  -10⁹ <= nums[i] <= 10⁹ 
#  -10⁹ <= lower <= upper <= 10⁹ 
#  
# 
#  Related Topics Array Two Pointers Binary Search Sorting 👍 788 👎 39

# class Solution:
#     def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
#         # 排序+固定起点二分终点+bisect(arr,val,start+1)
#         nums.sort()
#         res = 0
#         for i in range(len(nums)):
#             l = bisect.bisect_left(nums, lower - nums[i], i + 1)
#             r = bisect.bisect_right(nums, upper - nums[i], i + 1)
#             res += r - l
#         return res

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    # O(NLog(N))
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums1 = nums[:]
        nums1.sort()
        res = 0
        for i, x in enumerate(nums1):
            # if x < lower or x > upper:
            #     continue
            low = low_bound(nums1, i + 1, lower - x)
            high = low_bound(nums1, i + 1, upper - x + 1) - 1
            if high < low:
                continue
            res += high - low + 1
        return res


def low_bound(nums, left_bound, target):
    l, r = left_bound, len(nums) - 1
    while l <= r:
        mid = l + (r - l) // 2
        if nums[mid] < target:
            l = mid + 1
        else:
            r = mid - 1
    return l


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    s = Solution()
    print(s.countFairPairs([1, 7, 9, 2, 5], 11, 11))
    # print(s.countFairPairs([0, 1, 7, 4, 4, 5], 3, 6))
