#!/usr/bin/python3
# -*- coding: UTF-8 -*-

# source:  https://leetcode-cn.com/problems/find-number-of-ways-to-reach-the-k-th-stair
# source:  https://leetcode.com/problems/find-number-of-ways-to-reach-the-k-th-stair

# [3154]-find-number-of-ways-to-reach-the-k-th-stair

"""
给你有一个 非负 整数 k 。有一个无限长度的台阶，最低 一层编号为 0 。 

 虎老师有一个整数 jump ，一开始值为 0 。虎老师从台阶 1 开始，虎老师可以使用 任意 次操作，目标是到达第 k 级台阶。假设虎老师位于台阶 i ，一次
 操作 中，虎老师可以： 

 
 向下走一级到 i - 1 ，但该操作 不能 连续使用，如果在台阶第 0 级也不能使用。 
 向上走到台阶 i + 2ʲᵘᵐᵖ 处，然后 jump 变为 jump + 1 。 
 

 请你返回虎老师到达台阶 k 处的总方案数。 

 注意 ，虎老师可能到达台阶 k 处后，通过一些操作重新回到台阶 k 处，这视为不同的方案。 

 

 示例 1： 

 
 输入：k = 0 
 

 输出：2 

 解释： 

 2 种到达台阶 0 的方案为： 

 
 虎老师从台阶 1 开始。 
 
 执行第一种操作，从台阶 1 向下走到台阶 0 。 
 
 虎老师从台阶 1 开始。 
 
 执行第一种操作，从台阶 1 向下走到台阶 0 。 
 执行第二种操作，向上走 2⁰ 级台阶到台阶 1 。 
 执行第一种操作，从台阶 1 向下走到台阶 0 。 
 
 

 示例 2： 

 
 输入：k = 1 
 

 输出：4 

 解释： 

 4 种到达台阶 1 的方案为： 

 
 虎老师从台阶 1 开始，已经到达台阶 1 。 
 虎老师从台阶 1 开始。 
 
 执行第一种操作，从台阶 1 向下走到台阶 0 。 
 执行第二种操作，向上走 2⁰ 级台阶到台阶 1 。 
 
 虎老师从台阶 1 开始。 
 
 执行第二种操作，向上走 2⁰ 级台阶到台阶 2 。 
 执行第一种操作，向下走 1 级台阶到台阶 1 。 
 
 虎老师从台阶 1 开始。 
 
 执行第一种操作，从台阶 1 向下走到台阶 0 。 
 执行第二种操作，向上走 2⁰ 级台阶到台阶 1 。 
 执行第一种操作，向下走 1 级台阶到台阶 0 。 
 执行第二种操作，向上走 2¹ 级台阶到台阶 2 。 
 执行第一种操作，向下走 1 级台阶到台阶 1 。 
 
 

 

 提示： 

 
 0 <= k <= 10⁹ 
 

 Related Topics 位运算 记忆化搜索 数学 动态规划 组合数学 👍 9 👎 0

"""

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def waysToReachStair(self, k: int) -> int:
# leetcode submit region end(Prohibit modification and deletion)
