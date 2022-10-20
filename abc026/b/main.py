# -*- coding: utf-8 -*-
"""
解く前のメモ用
"""
from sys import setrecursionlimit
from math import pi

setrecursionlimit(10**7)

N = int(input())
R = sorted([int(input()) for _ in range(N)], reverse=True)
mul = 0
for i in range(N):
    if i % 2 == 0:
        mul += R[i] ** 2
        continue
    mul -= R[i] ** 2
ans = mul * pi
print(ans)
