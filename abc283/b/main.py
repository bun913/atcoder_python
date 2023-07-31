# -*- coding: utf-8 -*-
"""
解く前のメモ用
"""
from sys import setrecursionlimit

setrecursionlimit(10**7)
N = int(input())
A = list(map(int, input().split()))
ad = A[:]
Q = int(input())

for i in range(Q):
    q = list(map(int, input().split()))
    if q[0] == 1:
        ad[q[1]-1] = q[2]
        continue
    print(ad[q[1]-1])
