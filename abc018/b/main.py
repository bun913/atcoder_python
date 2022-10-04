# -*- coding: utf-8 -*-
"""
解く前のメモ用
"""
from sys import setrecursionlimit

setrecursionlimit(10**7)

S = input()
N = int(input())

ans = list(S)
for _ in range(N):
    l, r = list(map(int, input().split()))
    t = ans[l - 1 : r]
    t = t[::-1]
    ans = ans[: l - 1] + t + ans[r:]
print(*ans, sep="")
