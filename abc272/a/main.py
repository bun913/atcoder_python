# -*- coding: utf-8 -*-
"""
解く前のメモ用
"""
from sys import setrecursionlimit

setrecursionlimit(10**7)

N = int(input())
L = list(map(int, input().split()))
print(sum(L))
