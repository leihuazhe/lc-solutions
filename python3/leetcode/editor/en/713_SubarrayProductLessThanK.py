#!/usr/bin/python3
# -*- coding: UTF-8 -*-

# source:  https://leetcode-cn.com/problems/subarray-product-less-than-k
# source:  https://leetcode.com/problems/subarray-product-less-than-k

# [713]-subarray-product-less-than-k

"""
Given an array of integers nums and an integer k, return the number of 
contiguous subarrays where the product of all the elements in the subarray is strictly 
less than k. 

 
 Example 1: 

 
Input: nums = [10,5,2,6], k = 100
Output: 8
Explanation: The 8 subarrays that have product less than 100 are:
[10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6]
Note that [10, 5, 2] is not included as the product of 100 is not strictly less 
than k.
 

 Example 2: 

 
Input: nums = [1,2,3], k = 0
Output: 0
 

 
 Constraints: 

 
 1 <= nums.length <= 3 * 10⁴ 
 1 <= nums[i] <= 1000 
 0 <= k <= 10⁶ 
 

 Related Topics Array Sliding Window 👍 6797 👎 215

"""
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        #  1 <= nums[i] <= 1000
        if k <= 1:
            return 0

        ans = 0
        prod = 1
        l = 0
        for r, x in enumerate(nums):
            prod *= x
            while prod >= k:
                prod /= nums[l]
                l += 1
            ans += r - l + 1

        return ans


# leetcode submit region end(Prohibit modification and deletion)

if __name__ == '__main__':
    s = Solution()
    # print(s.numSubarrayProductLessThanK(nums=[10, 5, 2, 6], k=100))
    print(s.numSubarrayProductLessThanK(nums=[1, 2, 3], k=0))
