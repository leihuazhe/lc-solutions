#!/usr/bin/python3
# -*- coding: UTF-8 -*-

# source:  https://leetcode-cn.com/problems/find-all-anagrams-in-a-string
# source:  https://leetcode.com/problems/find-all-anagrams-in-a-string

# [438]-find-all-anagrams-in-a-string

"""
给定两个字符串 s 和 p，找到 s 中所有 p 的 异位词 的子串，返回这些子串的起始索引。不考虑答案输出的顺序。 

 异位词 指由相同字母重排列形成的字符串（包括相同的字符串）。 

 

 示例 1: 

 
输入: s = "cbaebabacd", p = "abc"
输出: [0,6]
解释:
起始索引等于 0 的子串是 "cba", 它是 "abc" 的异位词。
起始索引等于 6 的子串是 "bac", 它是 "abc" 的异位词。
 

 示例 2: 

 
输入: s = "abab", p = "ab"
输出: [0,1,2]
解释:
起始索引等于 0 的子串是 "ab", 它是 "ab" 的异位词。
起始索引等于 1 的子串是 "ba", 它是 "ab" 的异位词。
起始索引等于 2 的子串是 "ab", 它是 "ab" 的异位词。
 

 

 提示: 

 
 1 <= s.length, p.length <= 3 * 10⁴ 
 s 和 p 仅包含小写字母 
 

 Related Topics 哈希表 字符串 滑动窗口 👍 1426 👎 0

"""
from typing import List

# leetcode submit region begin(Prohibit modification and deletion)

"""
只要字母出现的频率一致,则认为找到了一个异位词
The occurrence of letters in consistent frequencies is considered as finding an anagram.

TODO: complexity

time

space

"""


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        p_freq = [0] * 26
        f_freq = [0] * 26
        for _, c in enumerate(p):
            p_freq[ord(c) - ord('a')] += 1

        res = []
        l = 0
        r = -1
        while r + 1 < len(s):
            #
            r += 1
            f_freq[ord(s[r]) - ord('a')] += 1
            #
            if r - l + 1 > len(p):
                f_freq[ord(s[l]) - ord('a')] -= 1
                l += 1
            #
            if r - l + 1 == len(p) and f_freq == p_freq:
                res.append(l)
                # l = r + 1

        return res


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    s = Solution()
    print(s.findAnagrams(s="cbaebabacd", p="abc"))
    print(s.findAnagrams(s="abab", p="ab"))
