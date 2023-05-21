# -*- coding: utf-8 -*-
"""
解く前のメモ用
"""
from sys import setrecursionlimit

setrecursionlimit(10**7)

S = list(input())
T = list(input())

for i in range(len(T)):
    if i >= len(S) or S[i] != T[i]:
        print(i+1)
        exit()
