# -*- coding: utf-8 -*-
"""
先頭K項のうちK番目に大きい値は先頭Kで最小の値
queをK個に保つことで、最小を取り出せばK番目に大きい値が求められる
"""
import heapq

N, K = list(map(int, input().split()))
P = list(map(int, input().split()))
que = P[:K]
heapq.heapify(que)
print(que[0])

for i in range(K, N):
    rm = heapq.heappop(que)
    n = P[i]
    heapq.heappush(que, max(rm, n))
    print(que[0])
