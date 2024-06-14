#!/usr/bin/python3
# -*- coding: UTF-8 -*-

# source:  https://leetcode-cn.com/problems/letter-combinations-of-a-phone-number
# source:  https://leetcode.com/problems/letter-combinations-of-a-phone-number

# [17]-letter-combinations-of-a-phone-number

"""
Given a string containing digits from 2-9 inclusive, return all possible letter 
combinations that the number could represent. Return the answer in any order. 

 A mapping of digits to letters (just like on the telephone buttons) is given 
below. Note that 1 does not map to any letters. 
 
 
 Example 1: 

 
Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
 

 Example 2: 

 
Input: digits = ""
Output: []
 

 Example 3: 

 
Input: digits = "2"
Output: ["a","b","c"]
 

 
 Constraints: 

 
 0 <= digits.length <= 4 
 digits[i] is a digit in the range ['2', '9']. 
 

 Related Topics Hash Table String Backtracking 👍 18388 👎 992

"""
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        letterMap = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        ans = []

        def dfs(i, path):
            if len(path) == len(digits):
                ans.append(''.join(path))
                return
            letters = letterMap[digits[i]]
            for letter in letters:
                path.append(letter)
                dfs(i + 1, path)
                path.pop()

        dfs(0, [])
        return ans


# leetcode submit region end(Prohibit modification and deletion)

if __name__ == '__main__':
    s = "abcdefg"
    print(s[:-1])  # 不包含 -1
    print(s[::-1])
    print(s[1:-1:3])

    n = len(s) - 13 % len(s)
    res = s[n:] + s[:n]

    s = Solution()
    print(s.letterCombinations("23"))
