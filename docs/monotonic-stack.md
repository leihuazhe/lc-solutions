# 单调栈

## 什么时候用

如果你发现要计算的内容涉及到 上一个更大(小)的元素或者下一个更大(小)的元素。

## 使用核心

> 及时去掉无用元素，保存栈中数据有序。

- 任何时候都要注意下标问题！例如如果 stack 存的是 index，就不要传递 value。

- 注意比较 value， 不是比较 index。

## 每天温度 Daily Temperatures
https://leetcode.com/problems/daily-temperatures/description/

### 从左往右遍历

一旦 t 小于等于栈顶了，意味着同时 t 小于等于栈里的任何数。当 t <= 栈顶，则 t 无法更新栈顶的答案，也无法更新栈里的其他内容，因为栈是单调的。

```python3
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0] * n
        st = []
        for i in range(n):
            t = temperatures[i]
            # 注意这里是比较值,不是比较 index 
            while st and t > temperatures[st[-1]]: // [!code highlight]
                j = st.pop()
                res[j] = i - j
            st.append(i)
        return res 
```

### 从右往左遍历

```python3
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0] * n
        st = []
        for i in range(n-1,-1,-1):
            t = temperatures[i]
            while st and t >= temperatures[st[-1]]: // [!code highlight]
                st.pop()
            if st:
                res[i] = st[-1] - i
            st.append(i)
        
        return res 
```

## 接雨水

找上一个更大的元素，在找的过程中填坑。 

https://leetcode.com/problems/trapping-rain-water/description/

![单调栈横向计算雨水面积](./assets/单调栈横向计算雨水面积.jpg)

```python3
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
                distance = (i - left - 1) // [!code highlight]
                print('left', left, 'middle', middle, 'right', h, 'distance', distance, 'dh', dh)
                res += dh * distance
            st.append(i)
        return res
```

## 其他题目


- 1475. 商品折扣后的最终价格 https://leetcode.cn/problems/final-prices-with-a-special-discount-in-a-shop/
- 901. 股票价格跨度 https://leetcode.cn/problems/online-stock-span/
- 1019. 链表中的下一个更大节点 https://leetcode.cn/problems/next-greater-node-in-linked-list/
- 1944. 队列中可以看到的人数 https://leetcode.cn/problems/number-of-visible-people-in-a-queue/
- 84. 柱状图中最大的矩形 https://leetcode.cn/problems/largest-rectangle-in-histogram/
- 1793. 好子数组的最大分数 https://leetcode.cn/problems/maximum-score-of-a-good-subarray/
- 85. 最大矩形 https://leetcode.cn/problems/maximal-rectangle/

### 课后作业题解：
- 901. 股票价格跨度 https://leetcode.cn/problems/online-stock-span/solution/shi-pin-yi-ge-shi-pin-jiang-tou-dan-diao-cuk7/
- 1019. 链表中的下一个更大节点 https://leetcode.cn/problems/next-greater-node-in-linked-list/solution/tu-jie-dan-diao-zhan-liang-chong-fang-fa-v9ab/
- 1944. 队列中可以看到的人数 https://leetcode.cn/problems/number-of-visible-people-in-a-queue/solution/dan-diao-zhan-de-ben-zhi-ji-shi-qu-diao-8tp3s/
- 84. 柱状图中最大的矩形 https://leetcode.cn/problems/largest-rectangle-in-histogram/solution/dan-diao-zhan-fu-ti-dan-pythonjavacgojsr-89s7/
- 1793. 好子数组的最大分数 https://leetcode.cn/problems/maximum-score-of-a-good-subarray/solution/liang-chong-fang-fa-dan-diao-zhan-shuang-24zl/

### 更多单调栈题目
- https://leetcode.cn/circle/discuss/9oZFK9/
