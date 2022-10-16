# -*- coding: utf-8 -*-
"""
解く前のメモ用
"""
from sys import setrecursionlimit

setrecursionlimit(10**7)
N = int(input())

for i in range(1, 8):
    for n in range(1, 10):
        N -= 1
        if N == 0:
            print(str(n) * i)
            exit()
