#!/usr/bin/python3
# -*- coding: UTF-8 -*-

# source:  https://leetcode-cn.com/problems/longest-repeating-character-replacement
# source:  https://leetcode.com/problems/longest-repeating-character-replacement

# [424]-longest-repeating-character-replacement

"""
You are given a string s and an integer k. You can choose any character of the 
string and change it to any other uppercase English character. You can perform 
this operation at most k times. 

 Return the length of the longest substring containing the same letter you can 
get after performing the above operations. 

 
 Example 1: 

 
Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.
 

 Example 2: 

 
Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
There may exists other ways to achieve this answer too. 

 
 Constraints: 

 
 1 <= s.length <= 10⁵ 
 s consists of only uppercase English letters. 
 0 <= k <= s.length 
 

 Related Topics Hash Table String Sliding Window 👍 10442 👎 496

"""


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = {}
        res = 0
        l = 0
        for r in range(len(s)):
            if s[l] != s[r]:
                l = r
            res = max(res, r - l + 1)

        return res


# leetcode submit region end(Prohibit modification and deletion)

if __name__ == '__main__':
    s = Solution()
    # print(s.characterReplacement("AAABBCCCCDDDD", 2))
    print(s.characterReplacement("AAABBC", 2))
