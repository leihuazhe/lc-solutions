#!/usr/bin/python3
# -*- coding: UTF-8 -*-

# source:  https://leetcode-cn.com/problems/container-with-most-water
# source:  https://leetcode.com/problems/container-with-most-water

# [11]-container-with-most-water

"""
You are given an integer array height of length n. There are n vertical lines 
drawn such that the two endpoints of the iᵗʰ line are (i, 0) and (i, height[i]). 

 Find two lines that together with the x-axis form a container, such that the 
container contains the most water. 

 Return the maximum amount of water a container can store. 

 Notice that you may not slant the container. 

 
 Example 1: 
 
 
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,
7]. In this case, the max area of water (blue section) the container can 
contain is 49.
 

 Example 2: 

 
Input: height = [1,1]
Output: 1
 

 
 Constraints: 

 
 n == height.length 
 2 <= n <= 10⁵ 
 0 <= height[i] <= 10⁴ 
 

 Related Topics Array Two Pointers Greedy 👍 28745 👎 1722

"""
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        res = 0
        while l < r:
            if height[l] <= height[r]:
                res = max(res, (r - l) * height[l])
                l += 1
            elif height[l] > height[r]:
                res = max(res, (r - l) * height[r])
                r -= 1

        return res

# leetcode submit region end(Prohibit modification and deletion)
