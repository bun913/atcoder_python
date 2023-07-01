# -*- coding: utf-8 -*-
"""
解く前のメモ用
"""
from sys import setrecursionlimit

setrecursionlimit(10**7)

S = list(map(int, input().split()))
so = sorted(S)

for i, s in enumerate(S):
    if s != so[i]:
        print("No")
        exit()
    if s < 100 or s > 676:
        print("No")
        exit()
    if s % 25 != 0:
        print("No")
        exit()
print("Yes")
