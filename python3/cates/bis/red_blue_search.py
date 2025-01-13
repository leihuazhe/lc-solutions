from typing import List


class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        """
        pos = find the first index > 0
        neg = find the first index < 0
        """

        # find the index that is the first one >= target.
        def lower_bound(nums, target):
            l, r = 0, len(nums) - 1
            while l <= r:
                mid = (l + r) // 2
                if nums[mid] < target:
                    l = mid + 1
                else:
                    r = mid - 1
            return r + 1  # l

        # > 0 --->  >= 1
        pos = lower_bound(nums, 1)
        # < 0 ---> >= 0 - 1
        neg = lower_bound(nums, 0) - 1

        # there's no positive numbers.
        if pos == len(nums) or nums[pos] < 0:
            pos = 0
        if neg == len(nums) or nums[pos] >= 0:
            neg = 0

        return max(pos, neg)


if __name__ == '__main__':
    s = Solution()
    s.maximumCount([-3, -2, -1, 0, 0, 1, 2])
    # s.maximumCount([-3, -2, -1, 0, 0, 1, 2])
    # s.maximumCount([5, 20, 66, 1314])
