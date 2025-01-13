from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # m: len(row)
        # n: len(col)
        m, n = len(board), len(board[0])
        directions = [{0, 1}, {0, -1}, {1, 0}, {-1, 0}]
        visited = set()  # (1,2)
        ans = False

        def dfs(i, j, index):
            print('checking letter ', word[index])
            if index == len(word) - 1:
                nonlocal ans
                ans = True
                print('Got it')
                return
            # decouple
            for (dx, dy) in directions:
                p = (i + dx, j + dy)
                # if index == 3:
                print('visited', visited)
                print('dx', dx, 'dy', dy)
                print(p)

                if not ans and p not in visited and p[0] >= 0 and p[0] < m and p[1] >= 0 and p[1] < n and board[p[0]][
                    p[1]] == word[index]:
                    visited.add(p)
                    dfs(p[0], p[1], index + 1)

        first_letter = word[0]

        for i in range(m):
            for j in range(n):
                if board[i][j] == first_letter:
                    visited.add((i, j))
                    dfs(i, j, 1)
                    if ans:
                        return ans
                    visited = set()
        return ans


if __name__ == '__main__':
    s = Solution()
    s.exist([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], word="ABCCED")
