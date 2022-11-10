# -*- coding: utf-8 -*-
"""
解く前のメモ用
"""
N = int(input())
S = [list(input()) for _ in range(N)]
for L in zip(*S):
    print(*reversed(L), sep="")
