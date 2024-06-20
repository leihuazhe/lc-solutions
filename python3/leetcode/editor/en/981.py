class Pair:
    def __init__(self, ts, value):
        self.ts = ts
        self.value = value


class TimeMap:

    def __init__(self):
        self.map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.map:
            self.map[key] = []
        pairs = self.map[key]
        pairs.append(Pair(timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        pairs = self.map[key]
        pair = findTarget(pairs, timestamp)
        return pair.value if pair.ts <= timestamp else ""


# <= timestamp
def findTarget(pairs, timestamp):
    l, r = 0, len(pairs) - 1
    while l <= r:
        mid = l + (r - l) // 2
        if pairs[mid].ts > timestamp:
            r = mid - 1
        else:
            l = mid + 1
    return pairs[r]


if __name__ == '__main__':
    s = TimeMap()
    #     ["TimeMap","set","get","get","set","get","get"]
    s.set("a", "bar", 1)
    s.set("x", "b", 3)
    s.get("b", 3)
    s.set("foo", "bar2", 4)
    s.get("foo", 4)
    s.get("foo", 5)

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
