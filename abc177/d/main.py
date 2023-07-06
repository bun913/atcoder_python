# -*- coding: utf-8 -*-
"""
友人関係ごとにグループを作って、最大の人数となるグループの人数が答え
つまり隣接成分の最大の大きさとなるかな
幅優先探索とかで答えを求めることはできるものの、NMが大きいのでTLEになる
ノードの関係を整理するのに便利なのがUnionFind
グループのリーダーを決めてしまい、リーダーが一致するかどうかが同一グループに所属しているか確認する
Unionはグループの統合、Findはリーダーの確認
グループ同士を統合するときも同様にリーダーを確認する
人数が少ない方のグループ所属者を全て人数が多い方のグループのリーダーの子分にする
グループの統合をO(logN)でする。
"""
from functools import reduce

# UnionFind


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
uni = UnionFind(N)
for i in range(M):
    A, B = map(int, input().split())
    # A,Bが友達関係であることを記録
    uni.merge(A-1, B-1)
friends_group = uni.groups()
# 最も人数の大きいグループのサイズを出す
ans = reduce(lambda x, y: max(x, y), map(len, friends_group))
print(ans)
