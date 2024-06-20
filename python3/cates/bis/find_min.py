from typing import List


def findMin(nums: List[int]) -> int:
    left, right = -1, len(nums) - 1  # 开区间 (-1, n-1)
    while left + 1 < right:  # 开区间不为空
        mid = (left + right) // 2
        if nums[mid] < nums[right]:  # 蓝色
            right = mid
        elif nums[mid] > nums[right]:  # 红色
            left = mid
        else:
            right -= 1
    print("index min:", right, "value", nums[right])
    return nums[right]


def find_min(nums):
    n = len(nums)
    l, r = 0, n - 2
    while l <= r:
        mid = l + (r - l) // 2
        if nums[mid] < nums[r + 1]:  # blue
            r = mid - 1
        elif nums[mid] > nums[r + 1]:  # red
            l = mid + 1
        else:
            # nums[mid] == nums[r]
            r -= 1

    print("index min:", l, "value", nums[l])
    return nums[l]


def find_minV2(nums):
    n = len(nums)
    l, r = 0, n - 2
    while l <= r:
        mid = l + (r - l) // 2
        if nums[mid] <= nums[-1]:  # blue
            r = mid - 1
        else:
            l = mid + 1

    print("index min:", l, "value", nums[l])
    return nums[l]


if __name__ == '__main__':
    nums = [0, 1, 2, 3, 4, 5]
    for i in range(len(nums)):
        print(i)

    find_minV2([2, 3, 4, 1])
    find_min([2, 2, 2, 3, 2, 2, 2])
    find_min([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1])
    # findMin([3, 1, 3])
    # find_min([3, 1, 3])
    # find_min([3, 3, 1, 3])
    # find_min([3, 3, 3, 1, 3])
    # find_min([4, 5, 6, 7, 8, 9, 0, 0])
