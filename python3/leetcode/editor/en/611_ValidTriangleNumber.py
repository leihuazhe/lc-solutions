#!/usr/bin/python3
# -*- coding: UTF-8 -*-

# source:  https://leetcode-cn.com/problems/valid-triangle-number
# source:  https://leetcode.com/problems/valid-triangle-number

# [611]-valid-triangle-number

"""
Given an integer array nums, return the number of triplets chosen from the 
array that can make triangles if we take them as side lengths of a triangle. 

 
 Example 1: 

 
Input: nums = [2,2,3,4]
Output: 3
Explanation: Valid combinations are: 
2,3,4 (using the first 2)
2,3,4 (using the second 2)
2,2,3
 

 Example 2: 

 
Input: nums = [4,2,3,4]
Output: 4
 

 
 Constraints: 

 
 1 <= nums.length <= 1000 
 0 <= nums[i] <= 1000 
 

 Related Topics Array Two Pointers Binary Search Greedy Sorting 👍 3806 👎 215

"""
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        ans = 0
        if n < 3:
            return ans

        for k in range(n - 1, -1, -1):
            c = nums[k]
            if nums[0] + nums[1] > c:
                ans += (k+1)*k*(k-1) //6
                break
            if nums[k-2] + nums[k-1] <= c:
                continue
            i = 0
            j = k-1
            while i < j:
                if nums[i] + nums[j] > c:
                    ans += (j-i)
                    j -= 1
                else:
                    i += 1
        return ans
# leetcode submit region end(Prohibit modification and deletion)
