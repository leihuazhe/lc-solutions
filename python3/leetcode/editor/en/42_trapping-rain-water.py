#!/usr/bin/python3
# -*- coding: UTF-8 -*-
from typing import List


# source:  https://leetcode-cn.com/problems/trapping-rain-water
# source:  https://leetcode.com/problems/trapping-rain-water

# [42]-trapping-rain-water

# Given n non-negative integers representing an elevation map where the width 
# of each bar is 1, compute how much water it can trap after raining. 
# 
#  
#  Example 1: 
#  
#  
# Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6
# Explanation: The above elevation map (black section) is represented by array [
# 0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) 
# are being trapped.
#  
# 
#  Example 2: 
# 
#  
# Input: height = [4,2,0,3,2,5]
# Output: 9
#  
# 
#  
#  Constraints: 
# 
#  
#  n == height.length 
#  1 <= n <= 2 * 10⁴ 
#  0 <= height[i] <= 10⁵ 
#  
# 
#  Related Topics Array Two Pointers Dynamic Programming Stack Monotonic Stack ?
# ? 31738 👎 506


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        res = 0
        st = []
        for i in range(len(height)):
            h = height[i]
            while st and h >= height[st[-1]]:
                middle = st.pop()
                if not st:
                    break
                left = st[-1]
                dh = min(height[left], h) - height[middle]
                distance = (i - left - 1)
                print('left', left, 'middle', middle, 'right', h, 'distance', distance, 'dh', dh)
                res += dh * distance
            st.append(i)
        return res

    # leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    s = Solution()
    # print(s.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
    print(s.trap([5, 2, 1, 0, 4, 1, 1, 6]))
