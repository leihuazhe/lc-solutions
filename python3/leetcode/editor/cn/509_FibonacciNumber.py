#!/usr/bin/python3
# -*- coding: UTF-8 -*-

"""
            1.确定dp数组（dp table）以及下标的含义

            2.确定递推公式

            3.dp数组如何初始化

            4.确定遍历顺序

            5.举例推导dp数组
"""

# source:  https://leetcode-cn.com/problems/fibonacci-number
# source:  https://leetcode.com/problems/fibonacci-number

# [509]-fibonacci-number

"""
斐波那契数 （通常用 F(n) 表示）形成的序列称为 斐波那契数列 。该数列由 0 和 1 开始，后面的每一项数字都是前面两项数字的和。也就是： 

 
F(0) = 0，F(1) = 1
F(n) = F(n - 1) + F(n - 2)，其中 n > 1
 

 给定 n ，请计算 F(n) 。 

 

 示例 1： 

 
输入：n = 2
输出：1
解释：F(2) = F(1) + F(0) = 1 + 0 = 1
 

 示例 2： 

 
输入：n = 3
输出：2
解释：F(3) = F(2) + F(1) = 1 + 1 = 2
 

 示例 3： 

 
输入：n = 4
输出：3
解释：F(4) = F(3) + F(2) = 2 + 1 = 3
 

 

 提示： 

 
 0 <= n <= 30 
 

 Related Topics 递归 记忆化搜索 数学 动态规划 👍 754 👎 0

"""


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    """
1.确定dp数组（dp table）以及下标的含义

            dp[i]的定义为：第i个数的斐波那契数值是dp[i]
            这里如果输入n,那就是 dp[n], dp 数组已存储的元素有 n + 1 个了.

2.确定递推公式
           状态转移方程 dp[i] = dp[i - 1] + dp[i - 2];

3.dp数组如何初始化
        dp[0] = 0;
        dp[1] = 1;

4.确定遍历顺序
    dp[i]是依赖 dp[i - 1] 和 dp[i - 2]，那么遍历的顺序一定是从前到后遍历的

5.举例推导dp数组
    n = 10
    0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55
    """

    def fib(self, n: int) -> int:
        if n <= 1: return n;
        dp = [0] * (n + 1)
        dp[0] = 0
        dp[1] = 1

        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]

        print(dp)
        return dp[n]

    # leetcode submit region end(Prohibit modification and deletion)
    def fib2(self, n: int) -> int:
        if n <= 1: return n
        # 为什么是 n + 1
        dp = [0] * (n + 1)
        dp[0] = 0
        dp[1] = 1

        for i in range(2, n + 1):
            sum = dp[0] + dp[1]
            dp[0] = dp[1]
            dp[1] = sum

        return dp[1]


# time 0(n)
# space O(n) => o(1)
if __name__ == '__main__':
    print(Solution().fib(2))  # [0, 1, 1]
    print(Solution().fib(10))  # [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
    print(Solution().fib(1000))
