# -*- coding: utf-8 -*-
"""
m枚の割引があるので順番付きのデータ構造で純粋に出し入れすればよし
"""
import heapq


class priorityqueue:
    """
    最大値を常にpopしたい場合は、init時に-1をかける
    """

    def __init__(self, initial_data=None):
        if initial_data:
            data = [-1 * x for x in initial_data]
            heapq.heapify(data)
            self._heap = data
        else:
            init_data = []
            heapq.heapfy(init_data)
            self._heap = init_data

    def is_empty(self):
        return len(self._heap) == 0

    def push(self, item):
        heapq.heappush(self._heap, item * -1)

    def pop(self):
        return -1 * heapq.heappop(self._heap)

    def get_list(self):
        return list(self._heap)


n, m = map(int, input().split())
a = list(map(int, input().split()))
hq = priorityqueue(a)
for _ in range(m):
    max_a = hq.pop()
    hq.push(max_a // 2)
ans = -sum(hq.get_list())
print(ans)
