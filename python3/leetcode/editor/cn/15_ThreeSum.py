#!/usr/bin/python3
# -*- coding: UTF-8 -*-

# source:  https://leetcode-cn.com/problems/3sum
# source:  https://leetcode.com/problems/3sum

# [15]-3sum

"""
⏰ eliminate the duplicates -->> sort the arrays.
we want to eliminate the duplicates. the solutions of this problem is to sort the array.

⏰ found the same element, then we should skip it.
   if nums[i] == nums[i-1] --> skip it.

⏰ sliding window to solve this problem.

⏰ in the two sum, we also should consider the duplicates, so we have to use a next method to shift our new l,r pointers.

sort the array -> O(nlogn)
two nested loops
Time: O(nlogn) + O(n2) ==> O(n2)

Space: O(1) or O(n)
"""
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # sort
        # nums = sorted(nums)
        nums.sort()
        n = len(nums)
        res = []
        # 3sum -> 2sum
        for i in range(n):
            # remove duplicates res
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            l = i + 1
            r = n - 1
            while l < r:
                val = nums[i] + nums[l] + nums[r]
                if val == 0:
                    res.append([nums[i], nums[l], nums[r]])
                    # reduce branches
                    l, r = self.next(l, r, nums)
                elif val > 0:
                    r -= 1
                else:
                    l += 1

        return res

    # 去重复逻辑
    def next(self, l: int, r: int, nums: List[int]):

        while l < r:
            if nums[l] == nums[l + 1]:
                l += 1
            elif nums[r] == nums[r - 1]:
                r -= 1
            else:
                l += 1
                r -= 1
                # 这一步不能漏的.
                return l, r

        return l, r


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    s = Solution()
    print(s.threeSum([-1, 0, 1, 2, -1, -4]))
    print(s.threeSum([0, 1, 1]))
