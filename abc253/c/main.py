# -*- coding: utf-8 -*-
"""
"""
from collections import defaultdict
import heapq

Q = int(input())
memo = defaultdict(int)

# 大きいものと小さい者を管理するためのheapq
mins = []
maxes = []

heapq.heapify(mins)
heapq.heapify(maxes)
for _ in range(Q):
    query = input().split()
    if query[0] == "1":
        _, x = query
        x = int(x)
        memo[x] += 1
        heapq.heappush(mins, x)
        heapq.heappush(maxes, -x)
        continue
    if query[0] == "2":
        _, x, c = query
        x = int(x)
        c = int(c)
        del_cnt = min(c, memo[x])
        memo[x] -= del_cnt
        continue
    min_num = heapq.heappop(mins)
    max_num = heapq.heappop(maxes)
    while memo[min_num] == 0:
        min_num = heapq.heappop(mins)
    while memo[-max_num] == 0:
        max_num = heapq.heappop(maxes)
    print(-max_num - min_num)
    # 戻す
    heapq.heappush(mins, min_num)
    heapq.heappush(maxes, max_num)
