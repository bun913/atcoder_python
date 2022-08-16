# -*- coding: utf-8 -*-
"""
解く前のメモ

無効グラフ
自分より頂点番号が小さい隣接頂点がちょうど1つ存在する

普通に行けばNが10の6乗、Mも10**6なので全探索は無理
それぞれNは線形にループしてMで自分より小さいのを探すのを二部探索で行けば間に合いそう
(それでもPythonならpypy3でギリギリ間に合うかって感じ)
"""
from bisect import bisect

N, M = list(map(int, input().split()))
memo = dict([(i+1, []) for i in range(N)])

# 無効グラフを作成
for _ in range(M):
    a, b = list(map(int, input().split()))
    memo[a].append(b)
    memo[b].append(a)

# 各頂点から条件を満たすか二部探索
ans = 0
for vert, points in memo.items():
    _sorted = sorted(points)
    ind = bisect(_sorted, vert)
    if ind == 1:
        ans += 1
print(ans)
