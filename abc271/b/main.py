# -*- coding: utf-8 -*-
"""
解く前のメモ用
"""
from sys import setrecursionlimit

setrecursionlimit(10**7)

N, Q = list(map(int, input().split()))
A = []
for _ in range(N):
    l = list(map(int, input().split()))
    A.append(l)
for i in range(Q):
    S, T = list(map(int, input().split()))
    ans = A[S - 1][T]
    print(ans)
