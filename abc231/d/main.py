# -*- coding: utf-8 -*-
"""
- 一つのノードから経路が3本以上あればだめ？
- だけでなくループしている場合もダメ
    - ループしているかどうかはすでに同じ隣接成分になっているときにさらに辺同士を繋げるとなる
"""


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
G = [[] for _ in range(N)]
un = UnionFind(N)
for _ in range(M):
    a, b = map(int, input().split())
    G[a-1].append(b-1)
    G[b-1].append(a-1)
    if un.same(a-1, b-1):
        # すでに同じ隣接成分になっているときさらに頂点を繋げるとループする
        print("No")
        exit()
    un.merge(a-1, b-1)

ans = 'Yes'
for i in range(N):
    if len(G[i]) >= 3:
        ans = 'No'
        break
print(ans)
