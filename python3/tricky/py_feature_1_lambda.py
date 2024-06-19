# py lambda 表达式
if __name__ == '__main__':
    s = ['abc', 'ab', 'a']
    s.sort(key=lambda x: len(x))
    print(s)
