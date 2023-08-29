# -*- coding: utf-8 -*-
"""
解く前のメモ用
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

# まずUnionFindで閉路がないことを確認しつつグラフを作る
un = UnionFind(N)
G = [[] for _ in range(N)]

for _ in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    # すでに同じグループなら閉路ができてしまう
    if un.same(a, b):
        print("No")
        exit()
    un.merge(a, b)
    G[a].append(b)
    G[b].append(a)

# そもそも全てのノードが連結になっているか
if len(un.groups()) != 1:
    print("No")
    exit()

# ノードの次数が2以下か確認
for edegs in G:
    if len(edegs) > 2:
        print("No")
        exit()
print("Yes")
