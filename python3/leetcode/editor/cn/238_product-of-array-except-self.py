#!/usr/bin/python3
# -*- coding: UTF-8 -*-
from typing import List


# source:  https://leetcode-cn.com/problems/product-of-array-except-self
# source:  https://leetcode.com/problems/product-of-array-except-self

# [238]-product-of-array-except-self

# 给你一个整数数组 nums，返回 数组 answer ，其中 answer[i] 等于 nums 中除 nums[i] 之外其余各元素的乘积 。 
# 
#  题目数据 保证 数组 nums之中任意元素的全部前缀元素和后缀的乘积都在 32 位 整数范围内。 
# 
#  请 不要使用除法，且在 O(n) 时间复杂度内完成此题。 
# 
#  
# 
#  示例 1: 
# 
#  
# 输入: nums = [1,2,3,4]
# 输出: [24,12,8,6]
#  
# 
#  示例 2: 
# 
#  
# 输入: nums = [-1,1,0,-3,3]
# 输出: [0,0,9,0,0]
#  
# 
#  
# 
#  提示： 
# 
#  
#  2 <= nums.length <= 10⁵ 
#  -30 <= nums[i] <= 30 
#  保证 数组 nums之中任意元素的全部前缀元素和后缀的乘积都在 32 位 整数范围内 
#  
# 
#  
# 
#  进阶：你可以在 O(1) 的额外空间复杂度内完成这个题目吗？（ 出于对空间复杂度分析的目的，输出数组 不被视为 额外空间。） 
# 
#  Related Topics 数组 前缀和 👍 1787 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = []
        prefix = [1] * n
        suffix = [1] * n
        for i in range(n):
            if i == 0:
                prefix[0] = 1
            else:
                prefix[i] = prefix[i - 1] * nums[i - 1]

        for i in range(n - 1, -1, -1):
            if i == n - 1:
                suffix[n - 1] = 1
            else:
                suffix[i] = suffix[i + 1] * nums[i + 1]

        for i in range(n):
            answer.append(prefix[i] * suffix[i])

        return answer

    # leetcode submit region end(Prohibit modification and deletion)
    def productExceptSelf2(self, nums: List[int]) -> List[int]:

        res = [1] * len(nums)

        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]

        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            # res[i] store the prefix
            # basis: cur = prefix * postfix
            res[i] = res[i] * postfix
            postfix *= nums[i]

        return res

    def productExceptSelf3(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n

        pre = 1
        for i in range(1, n):
            res[i] = pre
            pre *= nums[i]

        post = 1
        for i in range(n - 1, -1, -1):
            res[i] = res[i] * post
            post *= nums[i]

        return res


if __name__ == '__main__':
    s = Solution()
    print(s.productExceptSelf2([1, 2, 3, 4]))
    print(s.productExceptSelf2([-1, 1, 0, -3, 3]))
    print(s.productExceptSelf3([-1, 1, 0, -3, 3]))
