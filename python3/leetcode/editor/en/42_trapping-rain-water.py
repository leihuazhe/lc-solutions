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
    """
     基础方法
     - 当前 index 假设为一个宽为1的桶，它能接水的多少，取决于它左边的木板的高度和右边的木板的高度，取最小值，然后减去当前 index 本身的高度。
     - 实际是取决于**其左侧的最大高度** 和 **右侧的最大高度**。
     - 使用两个额外数组,第一个数组存储从最左边到第i个位置的最大高度。即，前缀最大值。
     - 第二个数组，存储从最右侧到 i 个位置的最大高度，及后缀最大值。
     - 对于每个前缀最大值，可以用上一个前缀最大值和当前的高度取最大值，取当前最大值。
- 前缀最大值 **`pre_max`** 和 后缀最大值 **`suf_max`**
    """

    def trapV1(self, height: List[int]) -> int:
        ans = 0
        n = len(height)
        pre_max = [0] * n
        suf_max = [0] * n
        for i in range(1, n):
            pre_max[i] = max(pre_max[i - 1], height[i])
        for i in range(n - 2, -1, -1):
            suf_max = max(suf_max[i + 1], height[i])

        for pre, h, suf in zip(pre_max, height, suf_max):
            ans += min(pre, suf) - h
        return ans

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
