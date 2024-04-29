# -*- coding: utf-8 -*-
"""
解く前のメモ用
"""
from sys import setrecursionlimit

setrecursionlimit(10**8)

N = int(input())
S = input()

ans = -1

for i in range(N-2):
    s = S[i:i+3]
    if s == "ABC":
        print(i+1)
        exit()
print(ans)
