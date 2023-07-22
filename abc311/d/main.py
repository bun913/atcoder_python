# -*- coding: utf-8 -*-
"""
"""
from collections import deque

N, M = map(int, input().split())
G = []
for _ in range(N):
    S = input().rstrip()
    G.append([1 if c == '.' else 0 for c in S])
# 探索済みか保持するset
seen = {(1, 1)}
# 通過したマスを保持するset
routes = {(1, 1)}
q = deque([(1, 1)])
dxy = [(1, 0), (-1, 0), (0, 1), (0, -1)]
while q:
    i, j = q.popleft()
    for di, dj in dxy:
        ni = i
        nj = j
        # いける限りその方向に進み続ける
        while G[ni+di][nj+dj] == 1:
            ni += di
            nj += dj
            # 通過したマスを追加
            routes.add((ni, nj))
        # いけるところまでいった先で、まだ探索していないマスをキューに追加
        if (ni, nj) not in seen:
            q.append((ni, nj))
            seen.add((ni, nj))
print(len(routes))
