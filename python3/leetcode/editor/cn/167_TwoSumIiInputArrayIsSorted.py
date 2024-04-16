#!/usr/bin/python3
# -*- coding: UTF-8 -*-

# source:  https://leetcode-cn.com/problems/two-sum-ii-input-array-is-sorted
# source:  https://leetcode.com/problems/two-sum-ii-input-array-is-sorted

# [167]-two-sum-ii-input-array-is-sorted

"""
1-indexed: 下标从 1 开始的
sorted in non-decreasing order: 非递减顺序排列
exactly one solution: 唯一的答案

给你一个下标从 1 开始的整数数组 numbers ，该数组已按 非递减顺序排列 ，请你从数组中找出满足相加之和等于目标数 target 的两个数。如果设这两个
数分别是 numbers[index1] 和 numbers[index2] ，则 1 <= index1 < index2 <= numbers.
length 。 

 以长度为 2 的整数数组 [index1, index2] 的形式返回这两个整数的下标 index1 和 index2。 

 你可以假设每个输入 只对应唯一的答案 ，而且你 不可以 重复使用相同的元素。 

 你所设计的解决方案必须只使用常量级的额外空间。 

 示例 1： 

 
输入：numbers = [2,7,11,15], target = 9
输出：[1,2]
解释：2 与 7 之和等于目标数 9 。因此 index1 = 1, index2 = 2 。返回 [1, 2] 。 

 示例 2： 

 
输入：numbers = [2,3,4], target = 6
输出：[1,3]
解释：2 与 4 之和等于目标数 6 。因此 index1 = 1, index2 = 3 。返回 [1, 3] 。 

 示例 3： 

 
输入：numbers = [-1,0], target = -1
输出：[1,2]
解释：-1 与 0 之和等于目标数 -1 。因此 index1 = 1, index2 = 2 。返回 [1, 2] 。
 

 

 提示： 

 
 2 <= numbers.length <= 3 * 10⁴ 
 -1000 <= numbers[i] <= 1000 
 numbers 按 非递减顺序 排列 
 -1000 <= target <= 1000 
 仅存在一个有效答案 
 

 Related Topics 数组 双指针 二分查找 👍 1191 👎 0

"""
from typing import List

"""

1-indexed: 下标从 1 开始的
sorted in non-decreasing order: 非递减顺序排列
exactly one solution: 唯一的答案

1. 窗口指针的选择 ----------->>>>> 本题的核心是,初始化时,窗口最大，然后往慢慢缩小窗口,直到找到结果.
2. left = 0, right = length - 1
"""


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        # r = 1
        # ⏰：core, 条件如何定义是最重要的!
        # 还有 r 的定义, 这种窗口叫
        # while r < len(numbers):

        r = len(numbers) - 1

        while l < r:
            # numbers
            val = numbers[l] + numbers[r]
            if val == target:
                return [l + 1, r + 1]
            if val > target:
                r -= 1
            else:
                l += 1

        return []


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    s = Solution()
    print(s.twoSum(numbers=[2, 7, 11, 15], target=9))
    print(s.twoSum(numbers=[2, 3, 4], target=6))
    print(s.twoSum(numbers=[5, 25, 75], target=100))
