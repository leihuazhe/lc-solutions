#!/usr/bin/python3
# -*- coding: UTF-8 -*-
from typing import List


# source:  https://leetcode-cn.com/problems/median-of-two-sorted-arrays
# source:  https://leetcode.com/problems/median-of-two-sorted-arrays

# [4]-median-of-two-sorted-arrays

# 给定两个大小分别为 m 和 n 的正序（从小到大）数组 nums1 和 nums2。请你找出并返回这两个正序数组的 中位数 。
#
#  算法的时间复杂度应该为 O(log (m+n)) 。
#
#
#
#  示例 1：
#
#
# 输入：nums1 = [1,3], nums2 = [2]
# 输出：2.00000
# 解释：合并数组 = [1,2,3] ，中位数 2
#
#
#  示例 2：
#
#
# 输入：nums1 = [1,2], nums2 = [3,4]
# 输出：2.50000
# 解释：合并数组 = [1,2,3,4] ，中位数 (2 + 3) / 2 = 2.5
#
#
#
#
#
#
#  提示：
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
#  Related Topics 数组 二分查找 分治 👍 7130 👎 0

# 解法1,将两个有序数组进行合并，然后再求中值。
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
    print(s.findMedianSortedArrays([1, 2, 4, 6], [2, 3, 5, 7, 9]))
    print(s.findMedianSortedArrays([1, 2, 4, 6], [2, 3, 5, 7]))  # 1,2,2,3,4,5,6,7
