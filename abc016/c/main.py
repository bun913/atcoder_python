# -*- coding: utf-8 -*-
"""
解く前のメモ用
"""
from collections import deque
from functools import reduce

N, M = map(int, input().split())
G = [[] for _ in range(N+1)]

# 隣接リストのグラフを作成
for _ in range(M):
    A, B = map(int, input().split())
    G[A].append(B)
    G[B].append(A)

for i in range(1, N+1):
    q = deque([i])
    distances = [-1] * (N+1)
    distances[i] = 0
    while q:
        cur = q.popleft()
        for nex in G[cur]:
            if distances[nex] != -1:
                continue
            distances[nex] = distances[cur] + 1
            q.append(nex)
    ans = reduce(lambda bef, cur: bef + 1 if cur == 2 else bef, distances, 0)
    print(ans)
