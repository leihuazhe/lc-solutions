from collections import Counter

if __name__ == '__main__':
    nums = [3, 3, 4, 4, 5, 6, 7, 7, 7, 7, 8, 8, 8, 8, 8, 8]
    c = Counter(nums)
    res = c.most_common(2)
    print(res)
