# -*- coding: utf-8 -*-
"""
解く前のメモ用
"""
from sys import setrecursionlimit

setrecursionlimit(10**7)
N, X = list(map(int, input().split()))
P = list(map(int, input().split()))
for i, p in enumerate(P):
    if p == X:
        print(i + 1)
        exit()
