#!/usr/bin/python3
# -*- coding: UTF-8 -*-

# source:  https://leetcode-cn.com/problems/min-cost-climbing-stairs
# source:  https://leetcode.com/problems/min-cost-climbing-stairs

# [746]-min-cost-climbing-stairs

"""
You are given an integer array cost where cost[i] is the cost of iᵗʰ step on a 
staircase. Once you pay the cost, you can either climb one or two steps. 

 You can either start from the step with index 0, or the step with index 1. 

 Return the minimum cost to reach the top of the floor. 

 
 Example 1: 

 
Input: cost = [10,15,20]
Output: 15
Explanation: You will start at index 1.
- Pay 15 and climb two steps to reach the top.
The total cost is 15.
 

 Example 2: 

 
Input: cost = [1,100,1,1,1,100,1,1,100,1]
Output: 6
Explanation: You will start at index 0.
- Pay 1 and climb two steps to reach index 2.
- Pay 1 and climb two steps to reach index 4.
- Pay 1 and climb two steps to reach index 6.
- Pay 1 and climb one step to reach index 7.
- Pay 1 and climb two steps to reach index 9.
- Pay 1 and climb one step to reach the top.
The total cost is 6.
 

 
 Constraints: 

 
 2 <= cost.length <= 1000 
 0 <= cost[i] <= 999 
 

 Related Topics Array Dynamic Programming 👍 11386 👎 1762

"""
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        """
        min(cost)
        min(cost[1:])
        """
        # return min(self.climb(cost), self.climb(cost[1:]))
        return self.climb(cost)

    def climb(self, cost: List[int]) -> int:
        """
        f[i]:
            cost: f[i-1]
            cost: f[i-2]
        f[i] = min(f[i-1],f[i-2])
        """
        n = len(cost)
        f = [0] * n
        f[0] = cost[0]
        f[1] = cost[1]
        for i in range(2, n):
            f[i] = min(f[i - 2], f[i - 1]) + cost[i]

        return min(f[n - 1], f[n - 2])


# leetcode submit region end(Prohibit modification and deletion)

if __name__ == '__main__':
    s = Solution()
    print(s.minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))
