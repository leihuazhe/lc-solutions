#!/usr/bin/python3
# -*- coding: UTF-8 -*-

# source:  https://leetcode-cn.com/problems/3sum
# source:  https://leetcode.com/problems/3sum

# [15]-3sum

"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]]
 such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0. 

 Notice that the solution set must not contain duplicate triplets. 

 
 Example 1: 

 
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not 
matter.
 

 Example 2: 

 
Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.
 

 Example 3: 

 
Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.
 

 
 Constraints: 

 
 3 <= nums.length <= 3000 
 -10⁵ <= nums[i] <= 10⁵ 
 

 Related Topics Array Two Pointers Sorting 👍 30495 👎 2826

"""
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # using sliding window , first, need to sort the nums.
        nums.sort()
        res = []
        for i in range(len(nums) - 2):
            #  i 重复问题
            if i > 0 and nums[i - 1] == nums[i]:
                continue
            l, r = i + 1, len(nums) - 1
            while l < r:
                v = nums[i] + nums[l] + nums[r]
                if v < 0:
                    l += 1
                elif v > 0:
                    r -= 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    # 涉及到重复的问题
                    l += 1
                    r -= 1
                    # TODO core: l < r
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1

        return res

# leetcode submit region end(Prohibit modification and deletion)
