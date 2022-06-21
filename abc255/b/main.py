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

N, K = list(map(int, input().split()))
A = list(map(int, input().split()))
xl = []
yl = []
for _ in range(N):
    x, y = list(map(int, input().split()))
    xl.append(x)
    yl.append(y)

min_dis = []

for i in range(N):
    # まず全ての点（人)にとって一番近い点を見つける
    # そこの点との距離をとっていき、それの最大値が答え
    near_dis = float('INF')
    x = xl[i]
    y = yl[i]
    for j in range(K):
        k = A[j] - 1
        kx = xl[k]
        ky = yl[k]
        ab = (x-kx) ** 2 + (y-ky) ** 2
        near_dis = min(near_dis, ab)
    min_dis.append(near_dis)
# 平方根で絶対距離の計算に戻す
ans = math.sqrt(max(min_dis))
print(ans)
