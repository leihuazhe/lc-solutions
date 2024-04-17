if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    res = all(n > 0 for n in nums)
    print(res)
    if not all(n > 0 for n in nums):
        print("not all")


# bisect_right