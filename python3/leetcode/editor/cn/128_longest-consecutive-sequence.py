#!/usr/bin/python3
# -*- coding: UTF-8 -*-
from typing import List


# source:  https://leetcode-cn.com/problems/longest-consecutive-sequence
# source:  https://leetcode.com/problems/longest-consecutive-sequence

# [128]-longest-consecutive-sequence

# 给定一个未排序的整数数组 nums ，找出数字连续的最长序列（不要求序列元素在原数组中连续）的长度。 
# 
#  请你设计并实现时间复杂度为 O(n) 的算法解决此问题。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [100,4,200,1,3,2]
# 输出：4
# 解释：最长数字连续序列是 [1, 2, 3, 4]。它的长度为 4。 
# 
#  示例 2： 
# 
#  
# 输入：nums = [0,3,7,2,5,8,4,6,0,1]
# 输出：9
#  
# 
#  
# 
#  提示： 
# 
#  
#  0 <= nums.length <= 10⁵ 
#  -10⁹ <= nums[i] <= 10⁹ 
#  
# 
#  Related Topics 并查集 数组 哈希表 👍 2095 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        res = 0
        while nums:
            value = nums.pop()
            l = value
            r = value
            # while 一直往后找
            while l - 1 in nums:
                nums.remove(l - 1)
                l -= 1
            while r + 1 in nums:
                nums.remove(r + 1)
                r += 1

            res = max(res, r - l + 1)
        return res

    # leetcode submit region end(Prohibit modification and deletion)
