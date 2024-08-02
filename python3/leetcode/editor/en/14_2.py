from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        s0 = strs[0]
        for i in range(len(s0)):
            for s in strs:
                if i == len(s) or s0[i] != s[i]:
                    return s0[:i]
        return s0


if __name__ == '__main__':
    s = Solution()
    print(s.longestCommonPrefix(["abb", "abc"]))
