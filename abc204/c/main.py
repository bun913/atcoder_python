"""
"""
from collections import deque

N, M = map(int, input().split())
G = [[] for _ in range(N)]

for _ in range(M):
    a, b = map(int, input().split())
    G[a-1].append(b-1)

# 答えには自分自身を含む
ans = 0
for start in range(N):
    q = deque([start])
    visited = [False] * N
    visited[start] = True
    while q:
        cur = q.popleft()
        for to in G[cur]:
            # すでに訪問済みの場合はスキップ
            if visited[to] is True:
                continue
            visited[to] = True
            q.append(to)
    ans += sum(visited)
print(ans)
