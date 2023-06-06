# -*- coding: utf-8 -*-
"""
解く前のメモ用
"""
from sys import setrecursionlimit

setrecursionlimit(10**7)
N = int(input())
A = list(map(int, input().split()))

ans = 0
for i in range(N):
    if i % 2 != 0:
        continue
    if A[i] % 2 != 0:
        ans += 1
print(ans)
