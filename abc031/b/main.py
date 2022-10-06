# -*- coding: utf-8 -*-
"""
解く前のメモ用
"""
from sys import setrecursionlimit

setrecursionlimit(10**7)
L, H = list(map(int, input().split()))
N = int(input())
A = [int(input()) for _ in range(N)]

for a in A:
    if a > H:
        print(-1)
        continue
    print(max(0, L - a))
