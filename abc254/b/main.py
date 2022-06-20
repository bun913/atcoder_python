# -*- coding: utf-8 -*-
"""
Atcoderの問題解く用

全ての組み合わせを列挙する方法
list(0...8)から2つを抜き出す
list(combinations(l, 2))

bit全探索でフラグが立っているかチェックする
if ((i >> j) & 1)
"""
from functools import reduce
from itertools import combinations
import math

# 再帰で普通にやってたらTLEになりそう
# 前の計算の結果をメモした方が良さそう
# 二次元配列で結果をメモしながら使っていく

N = int(input())
dp = [[0 for _ in range(i+1)] for i in range(N+1)]
# 初期化
dp[0][0] = 1


def f(i, j):
    if (j == 0) or (j == i):
        dp[i][j] = 1
        return 1
    # 前の計算結果を利用する
    a1 = dp[i-1][j-1]
    a2 = dp[i-1][j]
    v = a1 + a2
    dp[i][j] = v
    return v


ans = []
for i in range(N):
    lis = []
    for j in range(i+1):
        a = f(i, j)
        lis.append(a)
    print(*lis)
