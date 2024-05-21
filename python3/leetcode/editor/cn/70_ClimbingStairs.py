#!/usr/bin/python3
# -*- coding: UTF-8 -*-

# source:  https://leetcode-cn.com/problems/climbing-stairs
# source:  https://leetcode.com/problems/climbing-stairs

# [70]-climbing-stairs

"""
假设你正在爬楼梯。需要 n 阶你才能到达楼顶。 

 每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？ 

 

 示例 1： 

 
输入：n = 2
输出：2
解释：有两种方法可以爬到楼顶。
1. 1 阶 + 1 阶
2. 2 阶 

 示例 2： 

 
输入：n = 3
输出：3
解释：有三种方法可以爬到楼顶。
1. 1 阶 + 1 阶 + 1 阶
2. 1 阶 + 2 阶
3. 2 阶 + 1 阶
 

 

 提示： 

 
 1 <= n <= 45 
 

 Related Topics 记忆化搜索 数学 动态规划 👍 3518 👎 0

"""


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def climbStairs(self, n: int) -> int:
        if n <= 1:
            return 1
        dp = [0] * (n + 1)
        dp[1] = 1
        dp[2] = 2

        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]


"""
            1.确定dp数组（dp table）以及下标的含义
                dp[i] = dp[i-1] + 1
                dp[i] = dp[i-2] + 2

            2.确定递推公式

            3.dp数组如何初始化

            4.确定遍历顺序

            5.举例推导dp数组
"""


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':

    s = Solution()
    print(s.climbStairs(1))
    print(s.climbStairs(2))
    print(s.climbStairs(3))
    print(s.climbStairs(4))

