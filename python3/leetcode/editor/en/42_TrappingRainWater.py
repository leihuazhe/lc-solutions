#!/usr/bin/python3
# -*- coding: UTF-8 -*-

# source:  https://leetcode-cn.com/problems/trapping-rain-water
# source:  https://leetcode.com/problems/trapping-rain-water

# [42]-trapping-rain-water


from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def trap(self, height: List[int]) -> int:
        res = 0
        # dp 记录每个节点左右最大值
        dp_l = [0] * (len(height) + 1)
        dp_r = [0] * (len(height) + 1)
        # dp[i] = max(dp[i-1],height[i])
        dp_l[0] = 0
        for i in range(1, len(height) + 1):
            dp_l[i] = max(dp_l[i - 1], height[i - 1])

        dp_r[len(height) - 1] = 0
        for i in range(len(height) - 2, -1, -1):
            dp_r[i] = max(dp_r[i + 1], height[i + 1])

        for i in range(1, len(height) - 1):
            val = min(dp_l[i], dp_r[i]) - height[i]
            res += val if val > 0 else 0

        return res

    # leetcode submit region end(Prohibit modification and deletion)

    def trapBruteForce(self, height: List[int]) -> int:
        res = 0
        for i in range(len(height)):
            if i == 0 or i == len(height) - 1:
                continue
            l_max_h = max(height[:i])
            r_max_h = max(height[i + 1:])
            value = min(l_max_h, r_max_h) - height[i]
            if value > 0:
                res += value

        return res
