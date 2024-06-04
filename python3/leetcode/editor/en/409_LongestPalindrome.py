#!/usr/bin/python3
# -*- coding: UTF-8 -*-

# source:  https://leetcode-cn.com/problems/longest-palindrome
# source:  https://leetcode.com/problems/longest-palindrome

# [409]-longest-palindrome

"""
Given a string s which consists of lowercase or uppercase letters, return the 
length of the longest palindrome that can be built with those letters. 

 Letters are case sensitive, for example, "Aa" is not considered a palindrome. 

 
 Example 1: 

 
Input: s = "abccccdd"
Output: 7
Explanation: One longest palindrome that can be built is "dccaccd", whose 
length is 7.
 

 Example 2: 

 
Input: s = "a"
Output: 1
Explanation: The longest palindrome that can be built is "a", whose length is 1.

 

 
 Constraints: 

 
 1 <= s.length <= 2000 
 s consists of lowercase and/or uppercase English letters only. 
 

 Related Topics Hash Table String Greedy 👍 5352 👎 371

"""


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def longestPalindrome(self, s: str) -> int:
        # time: O(n)
        # space: O(min(52,len(set(s)))
        seen = set()
        res = 0
        for c in s:
            # we saw it before
            if c in seen:
                seen.remove(c)
                # pair
                res += 2
            else:
                seen.add(c)
        return res + 1 if seen else res

# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    s = Solution()
    # dccaccd
    print(s.longestPalindrome("abccccdd"))
    print(s.longestPalindrome("a"))
    print(s.longestPalindrome(""))
    print(s.longestPalindrome("bb"))
    print(s.longestPalindrome("bba"))
    print(s.longestPalindrome("bananas"))
