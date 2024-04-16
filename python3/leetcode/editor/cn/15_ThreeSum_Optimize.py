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


# 第一遍 2024.4.16

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        # 1.sort the array
        nums.sort()
        # 2.outer loop
        for i in range(n):
            # to eliminate the i duplicates
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            l = i + 1
            r = n - 1
            # 3. inner loop
            while l < r:
                val = nums[i] + nums[l] + nums[r]

                if val > 0:
                    r -= 1

                elif val < 0:
                    l += 1

                else:
                    res.append([nums[i], nums[l], nums[r]])
                    # update ptrs, only need to increment l
                    # [-2,-2,0,0,2,2]
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1

        return res


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    s = Solution()
    print(s.threeSum([-1, 0, 1, 2, -1, -4]))
    print(s.threeSum([0, 1, 1]))
