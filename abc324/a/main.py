# -*- coding: utf-8 -*-
"""
解く前のメモ用
"""
from sys import setrecursionlimit

setrecursionlimit(10**8)

N = int(input())
A = list(map(int, input().split()))

ans = "Yes"

for i in range(1, N):
    bef = A[i-1]
    cur = A[i]
    if bef != cur:
        print("No")
        exit()
print("Yes")
