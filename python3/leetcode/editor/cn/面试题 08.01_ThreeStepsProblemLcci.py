#!/usr/bin/python3
# -*- coding: UTF-8 -*-

# source:  https://leetcode-cn.com/problems/three-steps-problem-lcci
# source:  https://leetcode.com/problems/three-steps-problem-lcci

# [面试题 08.01]-three-steps-problem-lcci

"""
三步问题。有个小孩正在上楼梯，楼梯有n阶台阶，小孩一次可以上1阶、2阶或3阶。实现一种方法，计算小孩有多少种上楼梯的方式。结果可能很大，你需要对结果模10000
00007。 

 示例1: 

 
 输入：n = 3 
 输出：4
 说明: 有四种走法
 

 示例2: 

 
 输入：n = 5
 输出：13
 

 提示: 

 
 n范围在[1, 1000000]之间 
 

 Related Topics 记忆化搜索 数学 动态规划 👍 122 👎 0

"""

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def waysToStep(self, n: int) -> int:
# leetcode submit region end(Prohibit modification and deletion)
