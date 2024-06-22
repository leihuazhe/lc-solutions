class Solution:
    def getLucky(self, s: str, k: int) -> int:
        str_num = self.str_to_int_str(s)
        res = 0
        for _ in range(k):
            res = self.sum_str(str_num)
            str_num = str(res)
        return res

    def str_to_int_str(self, s: str):
        str_num = []
        for c in s:
            str_num.append(str(ord(c) - ord('a') + 1))
        return ''.join(str_num)

    def sum_str(self, s: str):
        return sum([int(c) for c in s])


if __name__ == '__main__':
    s = Solution()
    print(s.getLucky("leetcode", 2))
