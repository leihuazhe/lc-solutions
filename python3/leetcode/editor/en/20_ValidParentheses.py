#!/usr/bin/python3
# -*- coding: UTF-8 -*-

# source:  https://leetcode-cn.com/problems/valid-parentheses
# source:  https://leetcode.com/problems/valid-parentheses

# [20]-valid-parentheses

"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
 determine if the input string is valid. 

 An input string is valid if: 

 
 Open brackets must be closed by the same type of brackets. 
 Open brackets must be closed in the correct order. 
 Every close bracket has a corresponding open bracket of the same type. 
 

 
 Example 1: 

 
Input: s = "()"
Output: true
 

 Example 2: 

 
Input: s = "()[]{}"
Output: true
 

 Example 3: 

 
Input: s = "(]"
Output: false
 

 
 Constraints: 

 
 1 <= s.length <= 10⁴ 
 s consists of parentheses only '()[]{}'. 
 

 Related Topics String Stack 👍 23810 👎 1730

"""


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        pair = {'(': ')', '[': ']', '{': '}'}
        for c in s:
            if c in pair:
                st.append(c)
            else:
                # 栈没值,说明没有左开,而是直接又开了！不符合！
                if not st:
                    return False
                x = st.pop()
                if pair[x] != c:
                    return False
        return len(st) == 0

    # leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    s = Solution()
    print(s.isValid("(]"))
