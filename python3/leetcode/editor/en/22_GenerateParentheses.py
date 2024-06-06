#!/usr/bin/python3
# -*- coding: UTF-8 -*-

# source:  https://leetcode-cn.com/problems/generate-parentheses
# source:  https://leetcode.com/problems/generate-parentheses

# [22]-generate-parentheses

"""
Given n pairs of parentheses, write a function to generate all combinations of 
well-formed parentheses. 

 
 Example 1: 
 Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
 
 Example 2: 
 Input: n = 1
Output: ["()"]
 
 
 Constraints: 

 
 1 <= n <= 8 
 

 Related Topics String Dynamic Programming Backtracking 👍 20905 👎 922

"""
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        m = 2 * n
        ans = []
        path = []

        def dfs(i, left):
            if i == m:
                ans.append(''.join(path))
                return
            if left < n:
                path.append('(')
                dfs(i + 1, left + 1)
                path.pop()
            #

            if i - left < left:
                path.append(')')
                dfs(i + 1, left)
                path.pop()

        dfs(0, 0)
        return ans


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    s = Solution()
    print(s.generateParenthesis(2))
    # print(s.generateParenthesis(3))
    # print(s.generateParenthesis(4))
