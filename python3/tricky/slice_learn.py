"""

在Python中，切片（slicing）是一种非常强大和灵活的操作，用于从序列（如列表、元组、字符串等）中获取子序列。切片的语法为[start:stop:step]，其中：

start：起始索引，表示切片的开始位置。如果未提供，默认为0（序列的开头）。
stop：结束索引，表示切片的结束位置（但不包含该位置的元素）。如果未提供，默认为序列的长度。
step：步长，表示每次获取元素的间隔。如果未提供，默认为1。

"""

if __name__ == '__main__':
    res = [1, 2, 3, 4, 5, 6, 7]

    print(res[:])
    print(res[1:5])
    print(res[1::2])
    #
    print(res[3:])
    print(res[:3])
    #
    print(res[:-1])
    print(res[-4:-1])
    print(res[::-1])
