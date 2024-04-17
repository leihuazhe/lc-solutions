#!/usr/bin/python3
# -*- coding: UTF-8 -*-


# 159. Longest Substring with At Most Two Distinct Characters

"""
Given a string s , find the length of the longest substring t  that contains at most 2 distinct characters.
Example 1:

Input: "eceba"
Output: 3
Explanation: t is "ece" which its length is 3.
Example 2:

Input: "ccaabbb"
Output: 5
Explanation: t is "aabbb" which its length is 5.
Difficulty:

"""

"""
1.容易遗漏的一步, l 移除后,一定要从 dict 中删除。
1.1.怎么删? 找出 l 左边的那个删掉. ---> min_index
2. python3 中 dict 的用法(没有 map)
"""


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        max_len = 0
        dict = {}

        for r in range(len(s)):
            dict[s[r]] = r
            if len(dict) > 2:
                min_index = min(dict.values())
                l = min_index + 1
                del dict[s[min_index]]

            max_len = max(max_len, r - l + 1)

        return max_len


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    s = Solution()
    print('eceba', s.lengthOfLongestSubstring('eceba'))
    print('ccaabbb', s.lengthOfLongestSubstring('ccaabbb'))
    print('efccefcccccdsweerrrrrrfdddddddcc', s.lengthOfLongestSubstring('efccefcccccdsweerrrrrrfdddddddcc'))
