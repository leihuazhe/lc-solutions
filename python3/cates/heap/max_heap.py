class MaxPQ:
    def __init__(self):
        self.pq = []
        self.n = 0

    def __len__(self):
        return len(self.pq)

    def __str__(self):
        return str(self.pq)

    def insert(self, item):
        self.pq.append(item)
        self.n += 1
        self._swim(self.n)

    def remove(self):
        return self.pq.pop()

    def is_empty(self):
        return self.n == 0

    def size(self):
        return self.n

    def max(self):
        pass

    def del_max(self):

        # retrieve max from the top
        max = self.pq[1]
        # swap
        self.n -= 1
        self.swap(1, self.n)
        # release memory
        self.pq[self.n + 1] = None
        # sink down
        self._sink(1)

        return max

    def _swim(self, k):
        # while n // 2 and self.pq[n // 2] < self.pq[n]:
        #     self.swap(n, n / 2)
        #     n //= 2
        # pass
        while k > 1 and self.less(k // 2, k):
            self.swap(k // 2, k)
            k //= 2

    def _sink(self, k):
        while 2 * k <= self.n:
            j = 2 * k
            if j < self.n and self.less(j, j + 1):
                j += 1
            if not self.less(k, j):
                break
            self.swap(k, j)
            k = j

    def swap(self, i1, i2):
        self.pq[i1], self.pq[i2] = self.pq[i2], self.pq[i1]

    def less(self, i, j):
        return self.pq[i] < self.pq[j]
