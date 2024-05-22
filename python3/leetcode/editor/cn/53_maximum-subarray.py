#!/usr/bin/python3
# -*- coding: UTF-8 -*-
from typing import List


# source:  https://leetcode-cn.com/problems/maximum-subarray
# source:  https://leetcode.com/problems/maximum-subarray

# [53]-maximum-subarray

# 给你一个整数数组 nums ，请你找出一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。 
# 
#  子数组 是数组中的一个连续部分。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [-2,1,-3,4,-1,2,1,-5,4]
# 输出：6
# 解释：连续子数组 [4,-1,2,1] 的和最大，为 6 。
#  
# 
#  示例 2： 
# 
#  
# 输入：nums = [1]
# 输出：1
#  
# 
#  示例 3： 
# 
#  
# 输入：nums = [5,4,-1,7,8]
# 输出：23
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums.length <= 10⁵ 
#  -10⁴ <= nums[i] <= 10⁴ 
#  
# 
#  
# 
#  进阶：如果你已经实现复杂度为 O(n) 的解法，尝试使用更为精妙的 分治法 求解。 
# 
#  Related Topics 数组 分治 动态规划 👍 6669 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    # remove negative prefix. = sliding window.
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        res = nums[0]
        for i in range(len(nums)):
            cur_sum = nums[i]
            res = max(cur_sum, res)
            for j in range(i + 1, len(nums)):
                cur_sum += nums[j]
                res = max(cur_sum, res)

        return res


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    s = Solution()
    print(s.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
    print(s.maxSubArray([-2, 1]))
