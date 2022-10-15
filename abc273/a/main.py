# -*- coding: utf-8 -*-
"""
解く前のメモ用
"""
from sys import setrecursionlimit

setrecursionlimit(10**7)

N = int(input())


def f(k):
    if k == 0:
        return 1
    else:
        return k * f(k - 1)


ans = f(N)
print(ans)
