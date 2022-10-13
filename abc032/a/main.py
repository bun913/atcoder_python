# -*- coding: utf-8 -*-
"""
解く前のメモ用
"""
from numpy import lcm, ceil
from sys import setrecursionlimit

setrecursionlimit(10**7)

a = int(input())
b = int(input())
n = int(input())

lc = lcm(a, b)
if n <= lc:
    print(lc)
    exit()
mul = int(ceil(n / lc))
ans = lc * mul
print(ans)
