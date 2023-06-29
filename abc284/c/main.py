# -*- coding: utf-8 -*-
"""
幅優先探索でゴールまで辿り着ける
順番に幅優先探索をするが、まだ訪問済みじゃない頂点がなくなったら終了
Nが最大100,Mが最大10000なので、全探索でも間に合うはず
"""
from collections import deque

N, M = map(int, input().split())
G = [list() for _ in range(N)]
for _ in range(M):
    u, v = map(int, input().split())
    G[u-1].append(v-1)
    G[v-1].append(u-1)
visited = [False] * N
ans = 0
for i in range(N):
    if visited[i]:
        continue
    ans += 1
    visited[i] = True
    q = deque([i])
    while q:
        pos = q.popleft()
        for nex in G[pos]:
            if visited[nex] is False:
                visited[nex] = True
                q.append(nex)
print(ans)
