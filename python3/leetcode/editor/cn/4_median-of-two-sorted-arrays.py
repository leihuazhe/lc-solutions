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
    """
    Approach 3: Binary Search
    Use binary search to partition the smaller of the two input arrays into two parts.
    Find the partition of the larger array such that the sum of elements on the left side of the partition in both arrays is half of the total elements.
    Check if this partition is valid by verifying if the largest number on the left side is smaller than the smallest number on the right side.
    If the partition is valid, calculate and return the median.
    Time Complexity

    O(logm/logn)
    Space Complexity

    O(1)

    """

    def findMedianSortedArrays(self, nums1, nums2):
        n1 = len(nums1)
        n2 = len(nums2)

        # Ensure nums1 is the smaller array for simplicity
        if n1 > n2:
            return self.findMedianSortedArrays(nums2, nums1)

        n = n1 + n2
        left = (n1 + n2 + 1) // 2  # Calculate the left partition size
        low = 0
        high = n1

        while low <= high:
            mid1 = (low + high) // 2  # Calculate mid index for nums1
            mid2 = left - mid1  # Calculate mid index for nums2

            l1 = float('-inf')
            l2 = float('-inf')
            r1 = float('inf')
            r2 = float('inf')

            # Determine values of l1, l2, r1, and r2
            if mid1 < n1:
                r1 = nums1[mid1]
            if mid2 < n2:
                r2 = nums2[mid2]
            if mid1 - 1 >= 0:
                l1 = nums1[mid1 - 1]
            if mid2 - 1 >= 0:
                l2 = nums2[mid2 - 1]

            if l1 <= r2 and l2 <= r1:
                # The partition is correct, we found the median
                if n % 2 == 1:
                    return max(l1, l2)
                else:
                    return (max(l1, l2) + min(r1, r2)) / 2.0
            elif l1 > r2:
                # Move towards the left side of nums1
                high = mid1 - 1
            else:
                # Move towards the right side of nums1
                low = mid1 + 1

        return 0  # If the code reaches here, the input arrays were not sorted.

    #
    #
    #
    #

    def findMedianSortedArrays2(self, nums1: List[int], nums2: List[int]) -> float:
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
