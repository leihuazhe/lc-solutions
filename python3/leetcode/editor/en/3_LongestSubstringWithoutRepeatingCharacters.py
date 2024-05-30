#!/usr/bin/python3
# -*- coding: UTF-8 -*-

# source:  https://leetcode-cn.com/problems/longest-substring-without-repeating-characters
# source:  https://leetcode.com/problems/longest-substring-without-repeating-characters

# [3]-longest-substring-without-repeating-characters

"""
Given a string s, find the length of the longest substring without repeating 
characters. 

 
 Example 1: 

 
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
 

 Example 2: 

 
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
 

 Example 3: 

 
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a 
substring.
 

 
 Constraints: 

 
 0 <= s.length <= 5 * 10⁴ 
 s consists of English letters, digits, symbols and spaces. 
 

 Related Topics Hash Table String Sliding Window 👍 39332 👎 1865

"""


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        freq = set()
        l = 0
        res = 0
        for r in range(len(s)):
            while s[r] in freq:
                freq.remove(s[l])
                l += 1
            freq.add(s[r])
            res = max(res, r - l + 1)

        return res

# leetcode submit region end(Prohibit modification and deletion)
