# 快慢指针 - 链表成环 - 龟兔赛跑

如果链表有环，快慢指针就一定能在某个阶段相遇。快指针走2步，慢指针走一步。

## 快慢指针的应用

### 判断链表是否有环

- https://leetcode.com/problems/linked-list-cycle/

```python3
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow , fast = head, head
        # 如何 fast 能走到头，说明没有循环点
        # 同时要判断 fast 的 next 是否为空的问题
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True
        return False
```



### 寻找链表的中点

### 寻找链表的倒数第k个节点

### 寻找链表的入环点

- https://leetcode.com/problems/linked-list-cycle-ii/

![slow-fast](./assets/142_slow_fast.png)

```
从 head 到入口点的距离设为 x，入口点到相遇点的距离设为 y，环的的长度设为 n。

假设 slow 指针走过的距离为 t，那么 fast 指针走过的一定是 slow 指针的 2 倍，也就是 2t。

slow 指针从 head 出发走了 x 的距离到达入口点，然后可能走了 k1 圈，然后再次回到入口点，再走了 y 的距离到达相遇点和 fast 指针相遇。

t = x + k1 * n + y

fast 指针同理，fast 指针从 head 出发走了 x 的距离到达入口点，然后可能走了 k2 圈，然后再次回到入口点，再走了 y 的距离到达相遇点和 slow 指针相遇。

2t = x + k2 * n + y

上边两个等式做一个差，可以得到

t = (k2 - k1) * n

设 k = k2 - k1 ，那么 t = k * n。

把 t = k * n 代入到第一个式子 t = x + k1 * n + y 中。

k * n = x + k1 * n + y

移项，x = (k - k1) * n - y

取出一个 n 和 y 结合，x = (k - k1 - 1) * n + (n - y)

左边的含义就是从 head 到达入口点。

右边的含义， n - y 就是从相遇点到入口点的距离，(k - k1 - 1) * n 就是转 (k - k1 - 1) 圈。

左边右边的含义结合起来就是，从相遇点走到入口点，然后转 (k - k1 - 1) 圈后再次回到入口点的这段时间，刚好就等于从 head 走向入口点的时间。

```



### fast 指针每次移动3步是否可行，4，5?

