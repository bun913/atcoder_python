# -*- coding: utf-8 -*-
"""
解く前のメモ用
"""
from sys import setrecursionlimit
from itertools import combinations

setrecursionlimit(10**7)

N, M = list(map(int, input().split()))
memo = dict((i + 1, set()) for i in range(N))

for _ in range(M):
    L = list(map(int, input().split()))
    n, L = L[0], L[1:]
    for l, r in combinations(L, 2):
        memo[l].add(r)
        memo[r].add(l)
for k, v in memo.items():
    if len(v) != N - 1:
        print("No")
        exit()
print("Yes")
