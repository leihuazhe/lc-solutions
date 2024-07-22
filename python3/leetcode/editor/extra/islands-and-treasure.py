from typing import List


class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # m -> row: grid.length
        # n -> col: grid[i].length

        # r -> row
        # c -> col
        m = len(grid)
        n = len(grid[0])
        visited = set()

        def dfs(r, c, distance):
            # check if in area
            if not (0 <= r < m and 0 <= c < n):
                return
            val = grid[r][c]
            # skip water
            if val == -1:
                return distance

            # visited
            if val in visited:
                return distance

            visited.add(val)
            # found a treasure chest
            if val == 0:
                return distance

            return distance + min(dfs(r - 1, c, distance), dfs(r + 1, c, distance), dfs(r, c - 1, distance),
                                  dfs(r, c + 1, distance))

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2147483647:
                    grid[i][j] = dfs(i, j, 0)


if __name__ == '__main__':
    s = Solution()
    s.islandsAndTreasure(
        [[2147483647, -1, 0, 2147483647], [2147483647, 2147483647, 2147483647, -1], [2147483647, -1, 2147483647, -1],
         [0, -1, 2147483647, 2147483647]])
