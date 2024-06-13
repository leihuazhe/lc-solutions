#!/usr/bin/python3
# -*- coding: UTF-8 -*-
from typing import List


# source:  https://leetcode-cn.com/problems/maximum-count-of-positive-integer-and-negative-integer
# source:  https://leetcode.com/problems/maximum-count-of-positive-integer-and-negative-integer

# [2529]-maximum-count-of-positive-integer-and-negative-integer

# Given an array nums sorted in non-decreasing order, return the maximum 
# between the number of positive integers and the number of negative integers. 
# 
#  
#  In other words, if the number of positive integers in nums is pos and the 
# number of negative integers is neg, then return the maximum of pos and neg. 
#  
# 
#  Note that 0 is neither positive nor negative. 
# 
#  
#  Example 1: 
# 
#  
# Input: nums = [-2,-1,-1,1,2,3]
# Output: 3
# Explanation: There are 3 positive integers and 3 negative integers. The 
# maximum count among them is 3.
#  
# 
#  Example 2: 
# 
#  
# Input: nums = [-3,-2,-1,0,0,1,2]
# Output: 3
# Explanation: There are 2 positive integers and 3 negative integers. The 
# maximum count among them is 3.
#  
# 
#  Example 3: 
# 
#  
# Input: nums = [5,20,66,1314]
# Output: 4
# Explanation: There are 4 positive integers and 0 negative integers. The 
# maximum count among them is 4.
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= nums.length <= 2000 
#  -2000 <= nums[i] <= 2000 
#  nums is sorted in a non-decreasing order. 
#  
# 
#  
#  Follow up: Can you solve the problem in O(log(n)) time complexity? 
# 
#  Related Topics Array Binary Search Counting 👍 879 👎 51
def lowBound(nums: List[int]):
    # neg -> red
    # pos -> blue
    l, r = 0, len(nums) - 1
    while l <= r:
        mid = l + (r - l) // 2
        if nums[mid] < 0:  # red
            l = mid + 1
        else:
            r = mid - 1
    return l


def highBound(nums: List[int]):
    # neg -> red
    # pos -> blue
    l, r = 0, len(nums) - 1
    while l <= r:
        mid = l + (r - l) // 2
        if nums[mid] <= 0:  # red
            l = mid + 1
        else:
            r = mid - 1
    return r


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        neg = lowBound(nums) - 1
        pos = highBound(nums) + 1

        return max(neg + 1, len(nums) - pos)

    # leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    s = Solution()
    print(s.maximumCount([-2, -1, -1, 1, 2, 3]))
    print(s.maximumCount([-3, -2, -1, 0, 0, 1, 2]))
    print(s.maximumCount([-3, -2, -1, 1, 2]))
    print(s.maximumCount([5, 20, 66, 1314]))
