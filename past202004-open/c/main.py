# -*- coding: utf-8 -*-
"""
解く前のメモ用
Xの書かれている黒いますはX
2<=j<=2N-2に対してXは書かれていない黒います、左上、上、右上にXが書かれていればます
"""
from sys import setrecursionlimit

setrecursionlimit(10**7)

N = int(input())
S = [list(input()) for _ in range(N)]

for i in range(N - 1, 0, -1):
    for j in range(2, 2 * N - 1):
        x = i - 1
        y = j - 1
        s = set([S[x + 1][y - 1], S[x + 1][y], S[x + 1][y + 1]])
        should_ope = "X" in s and S[x][y] == "#"
        if should_ope is True:
            S[x][y] = "X"
# 答えの出力
[print("".join(S[i])) for i in range(N)]
