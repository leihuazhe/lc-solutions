#!/usr/bin/python3
# -*- coding: UTF-8 -*-

# source:  https://leetcode-cn.com/problems/koko-eating-bananas
# source:  https://leetcode.com/problems/koko-eating-bananas

# [875]-koko-eating-bananas

"""
Koko loves to eat bananas. There are n piles of bananas, the iᵗʰ pile has piles[
i] bananas. The guards have gone and will come back in h hours. 

 Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses 
some pile of bananas and eats k bananas from that pile. If the pile has less 
than k bananas, she eats all of them instead and will not eat any more bananas 
during this hour. 

 Koko likes to eat slowly but still wants to finish eating all the bananas 
before the guards return. 

 Return the minimum integer k such that she can eat all the bananas within h 
hours. 

 
 Example 1: 

 
Input: piles = [3,6,7,11], h = 8
Output: 4
 

 Example 2: 

 
Input: piles = [30,11,23,4,20], h = 5
Output: 30
 

 Example 3: 

 
Input: piles = [30,11,23,4,20], h = 6
Output: 23
 

 
 Constraints: 

 
 1 <= piles.length <= 10⁴ 
 piles.length <= h <= 10⁹ 
 1 <= piles[i] <= 10⁹ 
 

 Related Topics Array Binary Search 👍 10409 👎 634

"""
import math
from math import inf
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # time: O(NLogN)
        piles.sort()
        res = inf
        l = 1
        r = piles[len(piles) - 1]

        while l <= r:
            speed = l + (r - l) // 2
            cost = 0
            for p in piles:
                cost += math.ceil(p / speed)
            if cost <= h:
                res = min(res, speed)
                r = speed - 1
            else:
                l = speed + 1

        return res

    # leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    # print(math.ceil(11/3))
    s = Solution()
    # print(s.minEatingSpeed([3, 6, 7, 11], 8))
    # print(s.minEatingSpeed([30, 11, 23, 4, 20], 5))
    # print(s.minEatingSpeed([30, 11, 23, 4, 20], 6))
    print(s.minEatingSpeed(
        [332484035, 524908576, 855865114, 632922376, 222257295, 690155293, 112677673, 679580077, 337406589, 290818316,
         877337160, 901728858, 679284947, 688210097, 692137887, 718203285, 629455728, 941802184], 823855818))
