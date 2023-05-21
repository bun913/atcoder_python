# -*- coding: utf-8 -*-
"""
解く前のメモ用
"""
from sys import setrecursionlimit

setrecursionlimit(10**7)
H, W = list(map(int, input().split()))
ans = 0
for _ in range(H):
    S = list(input())
    ans += S.count("#")
print(ans)
