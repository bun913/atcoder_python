# -*- coding: utf-8 -*-
"""
各部屋から1の部屋までにまず繋がっているか
1: 全ての部屋（ノード）が1と同じ隣接成分にあるかどうか
2: そうなら、各部屋から1の部屋までの距離を求める
"""
from collections import deque


class UnionFind:
    def __init__(self, n):
        self.n = n
        self.parent_size = [-1]*n

    def leader(self, a):
        if self.parent_size[a] < 0:
            return a
        self.parent_size[a] = self.leader(self.parent_size[a])
        return self.parent_size[a]

    def merge(self, a, b):
        x, y = self.leader(a), self.leader(b)
        if x == y:
            return
        if abs(self.parent_size[x]) < abs(self.parent_size[y]):
            x, y = y, x
        self.parent_size[x] += self.parent_size[y]
        self.parent_size[y] = x

    def same(self, a, b):
        return self.leader(a) == self.leader(b)

    def size(self, a):
        return abs(self.parent_size[self.leader(a)])

    def groups(self):
        result = [[] for _ in range(self.n)]
        for i in range(self.n):
            result[self.leader(i)].append(i)
        return [r for r in result if r != []]


N, M = map(int, input().split())
uf = UnionFind(N)
G = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    # ユニオンファインド木を作りつつ、グラフも作る
    uf.merge(a-1, b-1)
    G[a].append(b)
    G[b].append(a)
# 1と全ての部屋がつながっているので、距離を求める
for i in range(1, N):
    if not uf.same(0, i):
        print("No")
        exit()
print("Yes")
# 訪問済みかを管理する配列
visited = [False]*(N+1)
visited[1] = True
# 答えを格納する配列
ans = [0]*(N+1)
q = deque([1])
while len(q) > 0:
    from_room = q.popleft()
    for to_room in G[from_room]:
        if visited[to_room] is False:
            visited[to_room] = True
            ans[to_room] = from_room
            q.append(to_room)
print(*ans[2:], sep="\n")
