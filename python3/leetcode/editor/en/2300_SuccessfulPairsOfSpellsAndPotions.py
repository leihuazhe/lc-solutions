#!/usr/bin/python3
# -*- coding: UTF-8 -*-

# source:  https://leetcode-cn.com/problems/successful-pairs-of-spells-and-potions
# source:  https://leetcode.com/problems/successful-pairs-of-spells-and-potions

# [2300]-successful-pairs-of-spells-and-potions

"""
You are given two positive integer arrays spells and potions, of length n and m 
respectively, where spells[i] represents the strength of the iᵗʰ spell and 
potions[j] represents the strength of the jᵗʰ potion. 

 You are also given an integer success. A spell and potion pair is considered 
successful if the product of their strengths is at least success. 

 Return an integer array pairs of length n where pairs[i] is the number of 
potions that will form a successful pair with the iᵗʰ spell. 

 
 Example 1: 

 
Input: spells = [5,1,3], potions = [1,2,3,4,5], success = 7
Output: [4,0,3]
Explanation:
- 0ᵗʰ spell: 5 * [1,2,3,4,5] = [5,10,15,20,25]. 4 pairs are successful.
- 1ˢᵗ spell: 1 * [1,2,3,4,5] = [1,2,3,4,5]. 0 pairs are successful.
- 2ⁿᵈ spell: 3 * [1,2,3,4,5] = [3,6,9,12,15]. 3 pairs are successful.
Thus, [4,0,3] is returned.
 

 Example 2: 

 
Input: spells = [3,1,2], potions = [8,5,8], success = 16
Output: [2,0,2]
Explanation:
- 0ᵗʰ spell: 3 * [8,5,8] = [24,15,24]. 2 pairs are successful.
- 1ˢᵗ spell: 1 * [8,5,8] = [8,5,8]. 0 pairs are successful. 
- 2ⁿᵈ spell: 2 * [8,5,8] = [16,10,16]. 2 pairs are successful. 
Thus, [2,0,2] is returned.
 

 
 Constraints: 

 
 n == spells.length 
 m == potions.length 
 1 <= n, m <= 10⁵ 
 1 <= spells[i], potions[i] <= 10⁵ 
 1 <= success <= 10¹⁰ 
 

 Related Topics Array Two Pointers Binary Search Sorting 👍 2527 👎 76

"""
from bisect import bisect_right
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        pass


# leetcode submit region end(Prohibit modification and deletion)

def bs_right(nums, target):
    l, r = 0, len(nums) - 1
    while l <= r:
        mid = l + (r - l) // 2
        if nums[mid] <= target:
            l = mid + 1
        else:
            r = mid - 1

    return l


if __name__ == '__main__':
    nums = [1, 2, 3, 5, 6]

    print(bisect_right(nums, 3))  # > target
    print(bisect_right(nums, 4))
    print(bs_right(nums, 3))
    print(bs_right(nums, 4))
