# -*- coding: utf-8 -*-
"""
解く前のメモ用
なくした整数が一位に定まるので、最初と最後の数字は考えないで良さそう
"""
N = int(input())
A = list(map(int, input().split()))
S = sorted(A)

for i in range(N-1):
    cur = S[i]
    nex = S[i+1]
    if cur + 1 != nex:
        print(cur+1)
        exit()
