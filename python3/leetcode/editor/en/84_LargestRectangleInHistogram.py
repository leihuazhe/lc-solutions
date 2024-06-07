#!/usr/bin/python3
# -*- coding: UTF-8 -*-

# source:  https://leetcode-cn.com/problems/largest-rectangle-in-histogram
# source:  https://leetcode.com/problems/largest-rectangle-in-histogram

# [84]-largest-rectangle-in-histogram

"""
Given an array of integers heights representing the histogram's bar height 
where the width of each bar is 1, return the area of the largest rectangle in the 
histogram. 

 
 Example 1: 
 
 
Input: heights = [2,1,5,6,2,3]
Output: 10
Explanation: The above is a histogram where width of each bar is 1.
The largest rectangle is shown in the red area, which has an area = 10 units.
 

 Example 2: 
 
 
Input: heights = [2,4]
Output: 4
 

 
 Constraints: 

 
 1 <= heights.length <= 10⁵ 
 0 <= heights[i] <= 10⁴ 
 

 Related Topics Array Stack Monotonic Stack 👍 17027 👎 275

"""
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        st = []
        res = 0
        min_height = 0
        for i in range(len(heights)):
            # out
            while st and heights[i] > st[-1][0]:
                st.pop()
            # in
            st.append((heights[i], min(min_height, heights[i])))
            res = max(res, st[0][0] * len(st))

        return res


# leetcode submit region end(Prohibit modification and deletion)

if __name__ == '__main__':
    s = Solution()
    # 2,1,5,6,2,3
    print(s.largestRectangleArea([2, 1, 5, 6, 2, 3]))
    print(s.largestRectangleArea([2, 1, 5, 6, 7, 3]))
