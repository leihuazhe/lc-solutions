#!/usr/bin/python3
# -*- coding: UTF-8 -*-

# source:  https://leetcode-cn.com/problems/minimum-size-subarray-sum
# source:  https://leetcode.com/problems/minimum-size-subarray-sum

# [209]-minimum-size-subarray-sum

"""
Given an array of positive integers nums and a positive integer target, return 
the minimal length of a subarray whose sum is greater than or equal to target. 
If there is no such subarray, return 0 instead. 

 
 Example 1: 

 
Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem 
constraint.
 

 Example 2: 

 
Input: target = 4, nums = [1,4,4]
Output: 1
 

 Example 3: 

 
Input: target = 11, nums = [1,1,1,1,1,1,1,1]
Output: 0
 

 
 Constraints: 

 
 1 <= target <= 10⁹ 
 1 <= nums.length <= 10⁵ 
 1 <= nums[i] <= 10⁴ 
 

 
Follow up: If you have figured out the 
O(n) solution, try coding another solution of which the time complexity is 
O(n log(n)).

 Related Topics Array Binary Search Sliding Window Prefix Sum 👍 12530 👎 432

"""
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # Input: target = 7, nums = [2,3,1,2,4,3]
        n = len(nums)
        l, r = 0, 0
        total_sum = 0  # 滑动窗口内的元素和
        min_len = len(nums) + 1
        while r < n:
            total_sum += nums[r]
            r += 1
            while total_sum >= target:
                if r - l < min_len:
                    min_len = r - l
                total_sum -= nums[l]
                l += 1

        return min_len if min_len < len(nums) + 1 else 0

# leetcode submit region end(Prohibit modification and deletion)

if __name__ == '__main__':
    s = Solution()
    print(s.minSubArrayLen(7, [2, 3, 1, 2, 4, 3]))
    print(s.minSubArrayLen(4, [1, 4, 4]))
    print(s.minSubArrayLen(11, [1, 1, 1, 1, 1, 1, 1, 1]))