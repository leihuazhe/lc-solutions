#!/usr/bin/python3
# -*- coding: UTF-8 -*-
from collections import defaultdict


# source:  https://leetcode-cn.com/problems/permutation-in-string
# source:  https://leetcode.com/problems/permutation-in-string

# [567]-permutation-in-string

# Given two strings s1 and s2, return true if s2 contains a permutation of s1, 
# or false otherwise. 
# 
#  In other words, return true if one of s1's permutations is the substring of 
# s2. 
# 
#  
#  Example 1: 
# 
#  
# Input: s1 = "ab", s2 = "eidbaooo"
# Output: true
# Explanation: s2 contains one permutation of s1 ("ba").
#  
# 
#  Example 2: 
# 
#  
# Input: s1 = "ab", s2 = "eidboaoo"
# Output: false
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= s1.length, s2.length <= 10⁴ 
#  s1 and s2 consist of lowercase English letters. 
#  
# 
#  Related Topics Hash Table Two Pointers String Sliding Window 👍 11191 👎 404


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False
        s1_count, s2_count = defaultdict(int), defaultdict(int)
        for i in range(len(s1)):
            s1_count[s1[i]] += 1
            s2_count[s2[i]] += 1
        if s1_count == s2_count:
            return True
        l = 0
        #  take in r to the dict, and take out l from the dict.
        #  r value +1, l value -1
        #  窗口达到一定的程度后,再 划动
        for r in range(len(s1), len(s2)):
            # s[r] 可能不存在 default dict
            s2_count[s2[r]] += 1
            s2_count[s2[l]] -= 1
            if s2_count[s2[l]] == 0:
                s2_count.pop(s2[l])
            l += 1

            if s1_count == s2_count:
                return True

        return False


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    s = Solution()
print(s.checkInclusion("ab", "eidboaoo"))
print(s.checkInclusion("ab", "eidbaooo"))
