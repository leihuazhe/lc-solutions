#!/usr/bin/python3
# -*- coding: UTF-8 -*-


# source:  https://leetcode-cn.com/problems/lru-cache
# source:  https://leetcode.com/problems/lru-cache

# [146]-lru-cache

# Design a data structure that follows the constraints of a Least Recently Used 
# (LRU) cache. 
# 
#  Implement the LRUCache class: 
# 
#  
#  LRUCache(int capacity) Initialize the LRU cache with positive size capacity. 
# 
#  int get(int key) Return the value of the key if the key exists, otherwise 
# return -1. 
#  void put(int key, int value) Update the value of the key if the key exists. 
# Otherwise, add the key-value pair to the cache. If the number of keys exceeds 
# the capacity from this operation, evict the least recently used key. 
#  
# 
#  The functions get and put must each run in O(1) average time complexity. 
# 
#  
#  Example 1: 
# 
#  
# Input
# ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
# [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
# Output
# [null, null, null, 1, null, -1, null, -1, 3, 4]
# 
# Explanation
# LRUCache lRUCache = new LRUCache(2);
# lRUCache.put(1, 1); // cache is {1=1}
# lRUCache.put(2, 2); // cache is {1=1, 2=2}
# lRUCache.get(1);    // return 1
# lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
# lRUCache.get(2);    // returns -1 (not found)
# lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
# lRUCache.get(1);    // return -1 (not found)
# lRUCache.get(3);    // return 3
# lRUCache.get(4);    // return 4
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= capacity <= 3000 
#  0 <= key <= 10⁴ 
#  0 <= value <= 10⁵ 
#  At most 2 * 10⁵ calls will be made to get and put. 
#  
# 
#  Related Topics Hash Table Linked List Design Doubly-Linked List 👍 20571 👎 1
# 015


# leetcode submit region begin(Prohibit modification and deletion)

class Node:
    # 提高访问属性的速度，并节省内存
    # __slots__ = 'prev', 'next', 'key', 'value'

    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity

        self.dummy = Node()  # 哨兵节点
        self.dummy.prev = self.dummy
        self.dummy.next = self.dummy
        self.key_to_node = {}

    def move_to_front(self, x):
        x.prev = self.dummy
        x.next = self.dummy.next
        x.prev.next = x
        x.next.prev = x

    def remove(self, x):
        x.prev.next = x.next
        # x.next.pre = x.prev  # 找了很久，问题在这里
        x.next.prev = x.prev

    def get(self, key: int) -> int:
        node = self.get_node(key)
        # return node.value if self.get_node(key) else -1 这里调用了两次.
        return node.value if node else -1

    def put(self, key: int, value: int) -> None:
        node = self.get_node(key)
        if node:
            node.value = value
            return

        self.key_to_node[key] = node = Node(key, value)  # 新书
        self.move_to_front(node)

        if self.capacity < len(self.key_to_node):
            back_node = self.dummy.prev
            try:
                del self.key_to_node[back_node.key]
            except KeyError or ValueError:
                print("error")

            self.remove(back_node)

    def get_node(self, key):
        if key not in self.key_to_node:
            return None
        node = self.key_to_node[key]
        self.remove(node)
        self.move_to_front(node)
        return node

    def print_link_node(self):
        str_ = ""
        cur = self.dummy.next
        while cur and cur != self.dummy:
            str_ += str(cur.key) + '->'
            cur = cur.next
        print(str_)

    # Your LRUCache object will be instantiated and called as such:


# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# leetcode submit region end(Prohibit modification and deletion)

if __name__ == '__main__':
    s = LRUCache(2)
    s.put(1, 1)
    s.put(2, 2)
    s.print_link_node()
    print(s.get(1))
    s.print_link_node()

    s.put(3, 3)
    s.print_link_node()

    print(s.get(2))
    s.put(4, 4)
    s.print_link_node()
    print(s.get(1))
    print(s.get(3))
    print(s.get(4))
