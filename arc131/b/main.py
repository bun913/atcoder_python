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

H, W = list(map(int, input().split()))
dxy = [(-1, 0), (1, 0), (0, -1), (0, 1)]
full_colors = set(['1', '2', '3', '4', '5', ])
C = [list(input()) for _ in range(H)]
for i in range(H):
    for j in range(W):
        s = C[i][j]
        if s != '.':
            continue
        # 上下左右を見てない色を選ぶ
        colors = set()
        for dx, dy in dxy:
            a = i + dx
            b = j + dy
            if a < 0 or a > H-1 or b < 0 or b > W-1:
                continue
            colors.add(C[a][b])
        # 入っていない色を適当に選ぶ
        dif = full_colors.difference(colors)
        # 前後左右に何もない場合がある
        if len(dif) == 0:
            C[i][j] = '.'
        else:
            C[i][j] = list(dif)[0]
    print(*C[i], sep='')
