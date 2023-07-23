# -*- coding: utf-8 -*-
"""
T秒後に流れている音楽を求める
"""
from sys import setrecursionlimit
from itertools import accumulate
from bisect import bisect_left

setrecursionlimit(10**7)

N, T = list(map(int, input().split()))
A = list(map(int, input().split()))
tt = T % sum(A)
acc = list(accumulate(A))
for i in range(N):
    if acc[i] > tt:
        rest = acc[i] - tt
        print(i+1, A[i]-rest)
        exit()
