from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # 1.find the minimum index
        n = len(nums)
        min_index = find_min(nums, n)
        # 2.find the target
        if target > nums[-1]:
            l, r = 0, min_index - 1
        else:
            l, r = min_index, n - 1

        res_index = find_low_bound(nums, target, l, r)
        return res_index if nums[res_index] == target else -1


# [4,5,6,7,0,1,2]
def find_min(nums, n):
    l, r = 0, n - 2
    while l <= r:
        mid = l + (r - l) // 2
        if nums[mid] <= nums[-1]:  # blue 0,1,2 [4, 5, 6, 7, 8, 9, 0, 0]
            r = mid - 1
        else:
            l = mid + 1  # red
    return l  # r+1


# find nums[i] >= target
def find_low_bound(nums, target, l, r):
    while l <= r:
        mid = l + (r - l) // 2
        if nums[mid] < target:  # red
            l = mid + 1
        else:
            r = mid - 1
    return l  # r+ 1


if __name__ == '__main__':
    print(find_min([4, 5, 6, 7, 8, 9, 0, 0], 8))
    print(find_min([4], 1))
    # print(find_min([4, 5, 6, 7, 0, 0, 1, 2], 8))
    #
    # s = Solution()
    # print(s.search([4, 5, 6, 7, 0, 1, 2], 0))
