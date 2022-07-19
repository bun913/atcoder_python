# -*- coding: utf-8 -*-
"""
Atcoderの問題解く用

全ての組み合わせを列挙する方法
list(0...8)から2つを抜き出す
list(combinations(l, 2))

bit全探索でフラグが立っているかチェックする
if ((i >> j) & 1)
"""
from math import sqrt

N, D = list(map(int, input().split()))
X = [list(map(int, input().split())) for _ in range(N)]

ans = 0
# １個目の点
for i in range(N):
    # ２個目の点
    for j in range(i+1, N):
        s = 0
        # 行
        for d in range(D):
            a = X[i][d]
            b = X[j][d]
            s += (a-b) ** 2
        sqr = sqrt(s)
        if sqr.is_integer() is True:
            ans += 1
print(ans)
