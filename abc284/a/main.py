# -*- coding: utf-8 -*-
"""
解く前のメモ用
"""
from sys import setrecursionlimit

setrecursionlimit(10**7)

N = int(input())
S = [input() for _ in range(N)]
print(*S[::-1], sep="\n")
