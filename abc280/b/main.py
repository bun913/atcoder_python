# -*- coding: utf-8 -*-
"""
i番目までの和を保持しておき、それとの差を出していけば良い
"""
from sys import setrecursionlimit

setrecursionlimit(10**7)

N = int(input())
S = list(map(int, input().split()))
A = [S[0]]

for i in range(1, N):
    dif = S[i] - S[i-1]
    A.append(dif)
print(*A)
