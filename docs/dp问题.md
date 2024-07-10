# 基础动态规划问题

- 198 House Robber(打家劫舍) https://leetcode.com/problems/house-robber/description/
- 213 打家劫舍 II https://leetcode.cn/problems/house-robber-ii/

> 213 是一个是否选 X 的 varint problem.

- 70 爬楼梯 https://leetcode.cn/problems/climbing-stairs/

```
爬第 i 阶:
    前 i - 1 阶的爬法有 f(i-1) 次
    前 i - 2 阶的 爬法有 f(i-2) 次
当前阶的次数 f(i) 为从 f(i-1) 1步爬过来, 或从 f(i-2) 1次2步爬过来。
即: f(i) = f(i-1) + f(i-2)


**Explanation:**
- **Reaching the ith step:**
    - There are f(i-1) ways to reach the (i-1)th step.
    - There are f(i-2) ways to reach the (i-2)th step.

- To reach the ith step, we can either:
    - Take one step from the (i-1)th step (f(i-1) way).
    - Take two steps from the (i-2)th step (f(i-2) ways).

- Therefore, the total number of ways to reach the ith step (f(i)) is:
    - f(i) = f(i-1) + f(i-2)
```


- 746 使用最小花费爬楼梯 https://leetcode.cn/problems/min-cost-climbing-stairs/

```
时间复杂度：O(n)，其中 n 为 cost 的长度。由于每个状态只会计算一次，动态规划的时间复杂度 = 状态个数 × 单个状态的计算时间。本题状态个数等于 O(n)，单个状态的计算时间为 O(1)，所以动态规划的时间复杂度为 O(n)。
空间复杂度：O(n)。有多少个状态，memo 数组的大小就是多少。
```

- 377 组合总和 Ⅳ https://leetcode.cn/problems/combination-sum-iv/
- 2466 统计构造好字符串的方案数 https://leetcode.cn/problems/count-ways-to-build-good-strings/
- 2266 统计打字方案数 https://leetcode.cn/problems/count-number-of-texts/
- 740 删除并获得点数 https://leetcode.cn/problems/delete-and-earn/

- LCR 166. 珠宝的最高价值 https://leetcode.cn/problems/li-wu-de-zui-da-jie-zhi-lcof/