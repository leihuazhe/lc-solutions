from bisect import bisect_right, bisect_left


# low bound 红色区域最右边的一个
def lowerBound(nums: list[int], tar: int) -> int:
    l, r = 0, len(nums) - 1
    while l <= r:
        mid = (l + r) // 2
        if nums[mid] <= tar:
            l = mid + 1
        else:
            r = mid - 1
    return r  # l -1


# up bound 蓝色区域，最左边的一个
def upperBound(nums: list[int], tar: int) -> int:
    l, r = 0, len(nums) - 1
    while l <= r:
        mid = (l + r) // 2
        if nums[mid] >= tar:
            r = mid - 1
        else:
            l = mid + 1
    return l  # r + 1


if __name__ == '__main__':
    l1 = [1, 3, 5, 7, 9, 11, 11, 11, 13, 15, 17]

    # i, a[i-1] < x, a[i] >= x
    print(bisect_left(l1, 11, 9, 10))
    # i, a[i-1] <= x, a[i] > x
    print(bisect_right(l1, 11, 9))

    # <= 6
    print(lowerBound(l1, 10))
    # >= 6
    print(upperBound(l1, 10))
