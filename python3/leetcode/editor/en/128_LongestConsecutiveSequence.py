#!/usr/bin/python3
# -*- coding: UTF-8 -*-

# source:  https://leetcode-cn.com/problems/longest-consecutive-sequence
# source:  https://leetcode.com/problems/longest-consecutive-sequence

# [128]-longest-consecutive-sequence

"""
Given an unsorted array of integers nums, return the length of the longest 
consecutive elements sequence. 

 You must write an algorithm that runs in O(n) time. 

 
 Example 1: 

 
Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. 
Therefore its length is 4.
 

 Example 2: 

 
Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
 

 
 Constraints: 

 
 0 <= nums.length <= 10⁵ 
 -10⁹ <= nums[i] <= 10⁹ 
 

 Related Topics Array Hash Table Union Find 👍 19843 👎 1011

"""
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        l, r = 0, 0
        max_len = 0

        for i in range(len(nums)):
            x = nums[i]

        dup = 0
        while r + 1 < len(nums):
            r += 1
            if nums[r] == nums[r - 1] + 1:
                max_len = max(max_len, r - l + 1)
            elif nums[r] == nums[r - 1]:
                max_len = max(max_len, r - l + 1)
                dup += 1
            else:
                l = r
        return max_len - dup


# leetcode submit region end(Prohibit modification and deletion)

if __name__ == '__main__':
    print([] is None)
    s = Solution()
    print(s.longestConsecutive([0, 0]))
    print(s.longestConsecutive([100, 4, 200, 1, 3, 2]))
    print(s.longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]))
    print(s.longestConsecutive([1, 2, 0, 1]))
