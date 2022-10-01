# -*- coding: utf-8 -*-
"""
解く前のメモ用
"""
from sys import setrecursionlimit

setrecursionlimit(10**7)
N = int(input())
ans = format(N, "x")
ans = (str(ans)).zfill(2)
print(ans.upper())
