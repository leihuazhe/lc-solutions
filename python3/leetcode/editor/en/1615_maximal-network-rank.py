#!/usr/bin/python3
# -*- coding: UTF-8 -*-
from collections import defaultdict
from typing import List


# source:  https://leetcode-cn.com/problems/maximal-network-rank
# source:  https://leetcode.com/problems/maximal-network-rank

# [1615]-maximal-network-rank

# There is an infrastructure of n cities with some number of roads connecting 
# these cities. Each roads[i] = [ai, bi] indicates that there is a bidirectional 
# road between cities ai and bi. 
# 
#  The network rank of two different cities is defined as the total number of 
# directly connected roads to either city. If a road is directly connected to both 
# cities, it is only counted once. 
# 
#  The maximal network rank of the infrastructure is the maximum network rank 
# of all pairs of different cities. 
# 
#  Given the integer n and the array roads, return the maximal network rank of 
# the entire infrastructure. 
# 
#  
#  Example 1: 
# 
#  
# 
#  
# Input: n = 4, roads = [[0,1],[0,3],[1,2],[1,3]]
# Output: 4
# Explanation: The network rank of cities 0 and 1 is 4 as there are 4 roads 
# that are connected to either 0 or 1. The road between 0 and 1 is only counted once.
#  
# 
#  Example 2: 
# 
#  
# 
#  
# Input: n = 5, roads = [[0,1],[0,3],[1,2],[1,3],[2,3],[2,4]]
# Output: 5
# Explanation: There are 5 roads that are connected to cities 1 or 2.
#  
# 
#  Example 3: 
# 
#  
# Input: n = 8, roads = [[0,1],[1,2],[2,3],[2,4],[5,6],[5,7]]
# Output: 5
# Explanation: The network rank of 2 and 5 is 5. Notice that all the cities do 
# not have to be connected.
#  
# 
#  
#  Constraints: 
# 
#  
#  2 <= n <= 100 
#  0 <= roads.length <= n * (n - 1) / 2 
#  roads[i].length == 2 
#  0 <= ai, bi <= n-1 
#  ai != bi 
#  Each pair of cities has at most one road connecting them. 
#  
# 
#  Related Topics Graph 👍 2343 👎 365


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        adj = defaultdict(list)
        row = len(roads)

        for i, j in roads:
            adj[i].append(j)
        ans = 0
        visited = set()
        for city in adj.keys():
            road = [0]
            self.dfs(city, adj, road, visited)
            ans = max(ans, road[0])

        return ans

    def dfs(self, start, adj, road, visited):
        if start in adj:
            road[0] += len(adj[start])
            for x in adj[start]:
                self.dfs(x, adj, road, visited)


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    s = Solution()
    print(s.maximalNetworkRank(4, [[0, 1], [0, 3], [1, 2], [1, 3]]))
