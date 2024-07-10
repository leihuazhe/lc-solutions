#!/usr/bin/python3
# -*- coding: UTF-8 -*-

# source:  https://leetcode-cn.com/problems/climbing-stairs
# source:  https://leetcode.com/problems/climbing-stairs

# [70]-climbing-stairs

"""
You are climbing a staircase. It takes n steps to reach the top. 

 Each time you can either climb 1 or 2 steps. In how many distinct ways can you 
climb to the top? 

 
 Example 1: 

 
Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
 

 Example 2: 

 
Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
 

 
 Constraints: 

 
 1 <= n <= 45 
 

 Related Topics Math Dynamic Programming Memoization 👍 21887 👎 837

"""


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def climbStairs(self, n: int) -> int:
        """
        the i-th stairs:
            from (i-2)th: the sum ways of (i-2): f(i-2) + 1 way(2 step)
            from (i-1)th: the sum ways of (i-1): f(i-1) + 1 way(1 step)
            f(i) = f(i-2) + f(i-1)
        """
        if n <= 2:
            return n
        f = [0] * (n + 1)
        f[1] = 1
        f[2] = 2
        for i in range(3, n + 1):
            f[i] = f[i - 1] + f[i - 2]

        return f[n]

# leetcode submit region end(Prohibit modification and deletion)
