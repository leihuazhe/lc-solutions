from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        n = len(nums)
        min_index = find_min(nums, n)
        if target > nums[-1] and min_index > 0:
            l, r = 0, min_index - 1
        else:
            l, r = min_index, n - 1

        res_index = find_low_bound(nums, target, l, r)
        return True if nums[res_index] == target else False


def find_min(nums, n):
    l, r = 0, n - 2
    while l <= r:
        mid = l + (r - l) // 2
        if nums[mid] < nums[r + 1]:
            r = mid - 1
        elif nums[mid] > nums[r + 1]:
            l = mid + 1
        else:
            r -= 1
    return l


def find_low_bound(nums, target, l, r):
    while l <= r:
        mid = l + (r - l) // 2
        if nums[mid] < target:  # red
            l = mid + 1
        else:
            r = mid - 1
    return l


if __name__ == '__main__':
    s = Solution()
    print(s.search([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1], 2))
