from typing import List


class Solution:
    # 极简语法
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort(key=lambda x: len(x))
        s0 = strs[0]

        for j, c in enumerate(s0):
            for i in range(1, len(strs)):
                if strs[i][j] != c:
                    return s0[:j]
        return s0

    def longestCommonPrefix(self, strs: List[str]) -> str:
        trie = Trie()
        for s in strs:
            trie.insert(s)
        res = []
        trie.searchCommon(trie.root, res, len(strs))
        return ''.join(res)


class TreeNode:
    def __init__(self):
        self.childNode = [None] * 26
        self.cnt = 0


class Trie:
    def __init__(self):
        self.root = TreeNode()

    def insert(self, s: str):
        cur = self.root
        for c in s:
            idx = ord(c) - ord('a')
            if not cur.childNode[idx]:
                cur.childNode[idx] = TreeNode()
            nxt = cur.childNode[idx]
            nxt.cnt += 1
            cur = nxt

    def searchCommon(self, cur, res, n):
        for i, c in enumerate(cur.childNode):
            if c and c.cnt == n:
                res.append(chr(i + ord('a')))
                self.searchCommon(c, res, n)


if __name__ == '__main__':
    s = Solution()
    print(s.longestCommonPrefix(["flower", "flow", "flight"]))
