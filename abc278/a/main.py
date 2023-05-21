# -*- coding: utf-8 -*-
"""
解く前のメモ用
"""
from sys import setrecursionlimit

setrecursionlimit(10**7)

N, K = list(map(int, input().split()))
A = list(map(int, input().split()))
ans = A[:]

for _ in range(K):
    ans.pop(0)
    ans.append(0)
print(*ans)
