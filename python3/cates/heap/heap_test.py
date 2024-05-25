import heapq

if __name__ == '__main__':
    min_heap = []
    heapq.heappush(min_heap, 123)
    heapq.heappush(min_heap, 12)
    heapq.heappush(min_heap, 1)
    heapq.heappush(min_heap, 8)
    heapq.heappush(min_heap, 82)
    heapq.heappush(min_heap, 72)
    heapq.heappush(min_heap, 32)
    heapq.heapify(min_heap)

    while min_heap:
        print(heapq.heappop(min_heap))

    sorted_list1 = [1, 3, 5]
    sorted_list2 = [2, 4, 6]
    merged = heapq.merge(sorted_list1, sorted_list2)
    print(list(merged))  # 输出: [1, 2, 3, 4, 5, 6]
