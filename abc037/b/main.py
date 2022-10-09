# -*- coding: utf-8 -*-
"""
解く前のメモ用
"""
from sys import setrecursionlimit

setrecursionlimit(10**7)

N, Q = list(map(int, input().split()))
A = [0 for _ in range(N)]

for _ in range(Q):
    L, R, T = list(map(int, input().split()))
    for i in range(L - 1, R):
        A[i] = T
print(*A, sep="\n")
