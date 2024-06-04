#!/usr/bin/python3
# -*- coding: UTF-8 -*-
from typing import List


# source:  https://leetcode-cn.com/problems/evaluate-reverse-polish-notation
# source:  https://leetcode.com/problems/evaluate-reverse-polish-notation

# [150]-evaluate-reverse-polish-notation

# You are given an array of strings tokens that represents an arithmetic 
# expression in a Reverse Polish Notation. 
# 
#  Evaluate the expression. Return an integer that represents the value of the 
# expression. 
# 
#  Note that: 
# 
#  
#  The valid operators are '+', '-', '*', and '/'. 
#  Each operand may be an integer or another expression. 
#  The division between two integers always truncates toward zero. 
#  There will not be any division by zero. 
#  The input represents a valid arithmetic expression in a reverse polish 
# notation. 
#  The answer and all the intermediate calculations can be represented in a 32-
# bit integer. 
#  
# 
#  
#  Example 1: 
# 
#  
# Input: tokens = ["2","1","+","3","*"]
# Output: 9
# Explanation: ((2 + 1) * 3) = 9
#  
# 
#  Example 2: 
# 
#  
# Input: tokens = ["4","13","5","/","+"]
# Output: 6
# Explanation: (4 + (13 / 5)) = 6
#  
# 
#  Example 3: 
# 
#  
# Input: tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
# Output: 22
# Explanation: ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
# = ((10 * (6 / (12 * -11))) + 17) + 5
# = ((10 * (6 / -132)) + 17) + 5
# = ((10 * 0) + 17) + 5
# = (0 + 17) + 5
# = 17 + 5
# = 22
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= tokens.length <= 10⁴ 
#  tokens[i] is either an operator: "+", "-", "*", or "/", or an integer in the 
# range [-200, 200]. 
#  
# 
#  Related Topics Array Math Stack 👍 7572 👎 1070


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        op = ['+', '-', '*', '/']
        st = []
        #
        for c in tokens:
            if c in op:
                #
                v2 = int(st.pop())
                v1 = int(st.pop())
                if c == '+':
                    x = v1 + v2
                elif c == '-':
                    x = v1 - v2
                elif c == '*':
                    x = v1 * v2
                else:
                    x = int(v1 / v2)

                st.append(int(x))
            else:
                st.append(c)

        return st.pop()


# leetcode submit region end(Prohibit modification and deletion)

if __name__ == '__main__':
    print(eval("int(3+5)"))
    print(int(-1 / 100))
    s = Solution()
    print(s.evalRPN(["18"]))
    print(s.evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]))
    print(s.evalRPN(["2", "1", "+", "3", "*"]))
    print(s.evalRPN(["4", "13", "5", "/", "+"]))
