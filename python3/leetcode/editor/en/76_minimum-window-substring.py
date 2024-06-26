from collections import defaultdict


# !/usr/bin/python3
# -*- coding: UTF-8 -*-


# source:  https://leetcode-cn.com/problems/minimum-window-substring
# source:  https://leetcode.com/problems/minimum-window-substring

# [76]-minimum-window-substring

# Given two strings s and t of lengths m and n respectively, return the minimum 
# window substring of s such that every character in t (including duplicates) is 
# included in the window. If there is no such substring, return the empty string 
# "". 
# 
#  The testcases will be generated such that the answer is unique. 
# 
#  
#  Example 1: 
# 
#  
# Input: s = "ADOBECODEBANC", t = "ABC"
# Output: "BANC"
# Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' 
# from string t.
#  
# 
#  Example 2: 
# 
#  
# Input: s = "a", t = "a"
# Output: "a"
# Explanation: The entire string s is the minimum window.
#  
# 
#  Example 3: 
# 
#  
# Input: s = "a", t = "aa"
# Output: ""
# Explanation: Both 'a's from t must be included in the window.
# Since the largest window of s only has one 'a', return empty string.
#  
# 
#  
#  Constraints: 
# 
#  
#  m == s.length 
#  n == t.length 
#  1 <= m, n <= 10⁵ 
#  s and t consist of uppercase and lowercase English letters. 
#  
# 
#  
#  Follow up: Could you find an algorithm that runs in O(m + n) time? 
# 
#  Related Topics Hash Table String Sliding Window 👍 17713 👎 725


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    """
    # Input: s = "ADOBECODEBANC", t = "ABC"
    # Output: "BANC"
    """

    def minWindow(self, s: str, t: str) -> str:

        if len(t) > len(s): return ""

        freq = defaultdict(int)
        for c in t:
            freq[c] += 1

        l, r = 0, 0
        cnt = 0
        min_len = len(s) + 1
        res = ""
        while r < len(s):
            if freq[s[r]] > 0:
                cnt += 1
            # 这个作用是处理重复元素的
            freq[s[r]] -= 1
            r += 1

            while cnt == len(t):
                if r - l < min_len:
                    min_len = r - l
                    res = s[l:r + 1]
                if freq[s[l]] == 0:
                    cnt -= 1
                freq[s[l]] += 1
                l += 1
        return res

    # leetcode submit region end(Prohibit modification and deletion)

    def minWindow2(self, s: str, t: str) -> str:
        freq = defaultdict(int)
        for c in t:
            freq[c] += 1

        l, r = 0, 0
        min_len = len(s) + 1
        cnt = 0
        res = ""
        while r < len(s):
            if freq[s[r]] > 0:
                cnt += 1
            freq[s[r]] -= 1
            r += 1

            while cnt == len(t):
                if min_len > r - l + 1:
                    min_len = r - l
                    res = s[l:r]
                if freq[s[l]] == 0:
                    cnt -= 1
                freq[s[l]] += 1
                l += 1
        return res


if __name__ == '__main__':
    # print(ord('a'), ord('z'), ord('A'))
    s = Solution()
    print(s.minWindow2("ab", "a"))
    print(s.minWindow2("ADOBECODEBANC", "ABC"))
    print(s.minWindow("ACBBACA", "ABA"))
    # print(s.minWindow("ADOBECODEBANC", "ABC"))
    # print(s.minWindow("a", "a"))
    # print(s.minWindow("ab", "a"))
