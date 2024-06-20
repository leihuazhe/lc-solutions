#!/usr/bin/python3
# -*- coding: UTF-8 -*-
from typing import List


# source:  https://leetcode-cn.com/problems/median-of-two-sorted-arrays
# source:  https://leetcode.com/problems/median-of-two-sorted-arrays

# [4]-median-of-two-sorted-arrays

# Given two sorted arrays nums1 and nums2 of size m and n respectively, return 
# the median of the two sorted arrays. 
# 
#  The overall run time complexity should be O(log (m+n)). 
# 
#  
#  Example 1: 
# 
#  
# Input: nums1 = [1,3], nums2 = [2]
# Output: 2.00000
# Explanation: merged array = [1,2,3] and median is 2.
#  
# 
#  Example 2: 
# 
#  
# Input: nums1 = [1,2], nums2 = [3,4]
# Output: 2.50000
# Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
#  
# 
#  
#  Constraints: 
# 
#  
#  nums1.length == m 
#  nums2.length == n 
#  0 <= m <= 1000 
#  0 <= n <= 1000 
#  1 <= m + n <= 2000 
#  -10⁶ <= nums1[i], nums2[i] <= 10⁶ 
#  
# 
#  Related Topics Array Binary Search Divide and Conquer 👍 28142 👎 3128


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m, n = len(nums1), len(nums2)
        total = m + n
        merge_nums = [0] * (m + n)
        odd = (m + n) % 2 == 1
        l, r = 0, 0
        for i in range(m + n):
            if l < m and r < n:
                if nums1[l] <= nums2[r]:
                    merge_nums[i] = nums1[l]
                    l += 1
                else:
                    merge_nums[i] = nums2[r]
                    r += 1
            elif l < m:
                merge_nums[i] = nums1[l]
                l += 1
            else:
                merge_nums[i] = nums2[r]
                r += 1

        if odd:
            return merge_nums[total // 2]
        v1 = merge_nums[total // 2 - 1]
        v2 = merge_nums[total // 2]
        return (v1 + v2) / 2.0


# leetcode submit region end(Prohibit modification and deletion)

if __name__ == '__main__':
    s = Solution()
    print(s.findMedianSortedArrays([1, 2], [3, 4]))
    print(s.findMedianSortedArrays([1, 3], [2]))
    print(s.findMedianSortedArrays([1, 3, 7, 9], [2, 3, 6]))
