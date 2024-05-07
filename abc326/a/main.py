# -*- coding: utf-8 -*-
"""
解く前のメモ用
"""
from sys import setrecursionlimit

setrecursionlimit(10**8)

X, Y = map(int, input().split())

if Y - X > 0 and Y - X <= 2:
    print("Yes")
    exit()
if Y - X <= 0 and abs(Y-X) <= 3:
    print("Yes")
    exit()
print("No")
