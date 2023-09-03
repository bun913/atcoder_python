# -*- coding: utf-8 -*-
"""
税抜価格Xを忘れたので知りたい
N円を支払っている
Xが小数の場合は切り捨て
"""
from sys import setrecursionlimit
from math import ceil

setrecursionlimit(10**7)
N = int(input())
cand1 = 100 * N // 108
cand2 = cand1 + 1
if cand1 * 108 // 100 == N:
    print(cand1)
    exit()
if cand2 * 108 // 100 == N:
    print(cand2)
    exit()
print(":(")
