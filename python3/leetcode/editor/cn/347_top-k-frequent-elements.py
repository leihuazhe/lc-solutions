#!/usr/bin/python3
# -*- coding: UTF-8 -*-
from collections import defaultdict
from typing import List


# source:  https://leetcode-cn.com/problems/top-k-frequent-elements
# source:  https://leetcode.com/problems/top-k-frequent-elements

# [347]-top-k-frequent-elements

# 给你一个整数数组 nums 和一个整数 k ，请你返回其中出现频率前 k 高的元素。你可以按 任意顺序 返回答案。 
# 
#  
# 
#  示例 1: 
# 
#  
# 输入: nums = [1,1,1,2,2,3], k = 2
# 输出: [1,2]
#  
# 
#  示例 2: 
# 
#  
# 输入: nums = [1], k = 1
# 输出: [1] 
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums.length <= 10⁵ 
#  k 的取值范围是 [1, 数组中不相同的元素的个数] 
#  题目数据保证答案唯一，换句话说，数组中前 k 个高频元素的集合是唯一的 
#  
# 
#  
# 
#  进阶：你所设计算法的时间复杂度 必须 优于 O(n log n) ，其中 n 是数组大小。 
# 
#  Related Topics 数组 哈希表 分治 桶排序 计数 快速选择 排序 堆（优先队列） 👍 1837 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mp = defaultdict(int)
        for n in nums:
            mp[n] += 1
        mp_values = sorted(mp.values())
        value_res = []
        for i in reversed(sorted(mp_values)):
            k -= 1
            if k >= 0:
                value_res.append(i)

        res = []

        for ke, v in mp.items():
            if v in value_res:
                res.append(ke)

        return res

    def topKFrequent2(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for n in nums:
            count[n] = 1 + count.get(n, 0)
        for n, c in count.items():
            freq[c].append(n)

        # return freq[-k:]
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if (len(res)) == k:
                    return res

    # leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    ls = [1, 2, 3, 4, 5, 6, 7, 8]
    print(ls[-3:])
    s = Solution()
    print(s.topKFrequent2([1, 1, 1, 2, 2, 3], 2))
    print(s.topKFrequent2([1, 2, 3, 4, 5, 6, 7], 1))
