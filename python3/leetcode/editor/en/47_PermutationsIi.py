#!/usr/bin/python3
# -*- coding: UTF-8 -*-

# source:  https://leetcode-cn.com/problems/permutations-ii
# source:  https://leetcode.com/problems/permutations-ii

# [47]-permutations-ii

"""
Given a collection of numbers, nums, that might contain duplicates, return all 
possible unique permutations in any order. 

 
 Example 1: 

 
Input: nums = [1,1,2]
Output:
[[1,1,2],
 [1,2,1],
 [2,1,1]]
 

 Example 2: 

 
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
 

 
 Constraints: 

 
 1 <= nums.length <= 8 
 -10 <= nums[i] <= 10 
 

 Related Topics Array Backtracking 👍 8459 👎 143

"""
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []
        perm = []
        visited = [False] * n

        def backtrack(perms: List[int]):
            if len(perms) == n:
                res.append(perms[:])
                return

            for i in range(n):
                if visited[i]:
                    continue
                if i > 0 and nums[i] == nums[i - 1] and visited[i - 1]:
                    continue

                perms.append(nums[i])
                visited[i] = True
                backtrack(perms)
                perms.pop()
                visited[i] = False

        backtrack(perm)

        return res


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    s = Solution()
    print(s.permuteUnique([1, 1, 2]))
