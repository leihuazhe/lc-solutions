#!/usr/bin/python3
# -*- coding: UTF-8 -*-
from collections import deque
from typing import List


# source:  https://leetcode-cn.com/problems/sliding-window-maximum
# source:  https://leetcode.com/problems/sliding-window-maximum

# [239]-sliding-window-maximum

# You are given an array of integers nums, there is a sliding window of size k 
# which is moving from the very left of the array to the very right. You can only 
# see the k numbers in the window. Each time the sliding window moves right by one 
# position. 
# 
#  Return the max sliding window. 
# 
#  
#  Example 1: 
# 
#  
# Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
# Output: [3,3,5,5,6,7]
# Explanation: 
# Window position                Max
# ---------------               -----
# [1  3  -1] -3  5  3  6  7       3
#  1 [3  -1  -3] 5  3  6  7       3
#  1  3 [-1  -3  5] 3  6  7       5
#  1  3  -1 [-3  5  3] 6  7       5
#  1  3  -1  -3 [5  3  6] 7       6
#  1  3  -1  -3  5 [3  6  7]      7
#  
# 
#  Example 2: 
# 
#  
# Input: nums = [1], k = 1
# Output: [1]
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= nums.length <= 10⁵ 
#  -10⁴ <= nums[i] <= 10⁴ 
#  1 <= k <= nums.length 
#  
# 
#  Related Topics Array Queue Sliding Window Heap (Priority Queue) Monotonic 
# Queue 👍 18009 👎 668


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    # TODO 没有思路
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        # monotonous queue
        # 从左到右,从大到小, 从栈底到栈顶,从大到小
        # # From left to right, in descending order
        # #  From bottom to top of the stack, in descending order
        queue = deque()
        for i in range(len(nums)):
            # 1. out
            while queue and nums[i] >= nums[queue[-1]]:
                queue.pop()
            # 2. in
            queue.append(i)
            # sliding 如何移除左侧
            if i - queue[0] + 1 > k:
                queue.popleft()
            # 3. res
            if i >= k - 1:
                res.append(nums[queue[0]])

        return res

    # leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    s = Solution()
    print(s.maxSlidingWindow([5, 4, 3, 2, 1, 10, 13, 15], 3))
    print(s.maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3))
    print(s.maxSlidingWindow([1, -1], 1))
