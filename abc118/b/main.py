# -*- coding: utf-8 -*-
"""
解く前のメモ

どうもこうもただ数えるだけ
NもMも最大で30なので2重ループで余裕
"""
N, M = list(map(int, input().split()))

favorites = [0 for _ in range(M)]

for i in range(N):
    L = list(map(int, input().split()))
    for a in L[1:]:
        favorites[a-1] += 1
ans = favorites.count(N)
print(ans)
