# -*- coding: utf-8 -*-
"""
解く前のメモ用
"""
from sys import setrecursionlimit

setrecursionlimit(10**7)
S = input()
ans = 0
for s in S:
    if s == "v":
        ans += 1
        continue
    ans += 2
print(ans)
