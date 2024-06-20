#!/usr/bin/python3
# -*- coding: UTF-8 -*-

# source:  https://leetcode-cn.com/problems/roman-to-integer
# source:  https://leetcode.com/problems/roman-to-integer

# [13]-roman-to-integer

# Roman numerals are represented by seven different symbols: I, V, X, L, C, D 
# and M. 
# 
#  
# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000 
# 
#  For example, 2 is written as II in Roman numeral, just two ones added 
# together. 12 is written as XII, which is simply X + II. The number 27 is written as 
# XXVII, which is XX + V + II. 
# 
#  Roman numerals are usually written largest to smallest from left to right. 
# However, the numeral for four is not IIII. Instead, the number four is written as 
# IV. Because the one is before the five we subtract it making four. The same 
# principle applies to the number nine, which is written as IX. There are six 
# instances where subtraction is used: 
# 
#  
#  I can be placed before V (5) and X (10) to make 4 and 9. 
#  X can be placed before L (50) and C (100) to make 40 and 90. 
#  C can be placed before D (500) and M (1000) to make 400 and 900. 
#  
# 
#  Given a roman numeral, convert it to an integer. 
# 
#  
#  Example 1: 
# 
#  
# Input: s = "III"
# Output: 3
# Explanation: III = 3.
#  
# 
#  Example 2: 
# 
#  
# Input: s = "LVIII"
# Output: 58
# Explanation: L = 50, V= 5, III = 3.
#  
# 
#  Example 3: 
# 
#  
# Input: s = "MCMXCIV"
# Output: 1994
# Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= s.length <= 15 
#  s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M'). 
#  It is guaranteed that s is a valid roman numeral in the range [1, 3999]. 
#  
# 
#  Related Topics Hash Table Math String 👍 14044 👎 919


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def romanToInt(self, s: str) -> int:
        c = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        n = len(s)
        res = 0
        i = 0
        while i < n:
            if i != n - 1 and c[s[i]] < c[s[i + 1]]:
                res += c[s[i + 1]] - c[s[i]]
                i += 2
            else:
                res += c[s[i]]
                i += 1
        return res


# leetcode submit region end(Prohibit modification and deletion)

if __name__ == '__main__':
    s = Solution()
    print(s.romanToInt("III"))
