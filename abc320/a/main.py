# -*- coding: utf-8 -*-
"""
解く前のメモ用
"""
from sys import setrecursionlimit

setrecursionlimit(10**8)

A, B = list(map(int, input().split()))
ans = A ** B + B ** A
print(ans)
