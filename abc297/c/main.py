# -*- coding: utf-8 -*-
"""
解く前のメモ用
"""
from copy import deepcopy

H, W = map(int, input().split())
# 普通にやるだけで良さそう
S = [list(input()) for _ in range(H)]
C = deepcopy(S)
for i in range(H):
    for j in range(W-1):
        cur = C[i][j]
        nxt = C[i][j+1]
        if cur == 'T' and nxt == 'T':
            C[i][j] = 'P'
            C[i][j+1] = 'C'
for c in C:
    print(*c, sep='')
