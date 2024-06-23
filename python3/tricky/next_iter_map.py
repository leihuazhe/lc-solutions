from collections import OrderedDict

if __name__ == '__main__':
    map = {6: 6, 1: 1, 2: 2, 3: 3}
    key1 = next(iter(map))
    # map.move_to_end(key1)
    print(key1)
    map2 = OrderedDict()
    map2[6] = 6
    map2[1] = 1
    map2.move_to_end(6)
    print(next(iter(map2)))
