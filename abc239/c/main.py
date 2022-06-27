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

x1, y1, x2, y2 = list(map(int, input().split()))
a_cand = []
b_cand = []

# 求める点はa,bの2点からそれぞれ絶対距離が3と慣れば良い(xかyの方向に合計3進む)
for dx in range(-2, 3):
    if dx == 0:
        continue
    dys = []
    a = 3 - abs(dx)
    dys.append(a)
    dys.append(-a)
    for dy in dys:
        ax = x1 + dx
        ay = y1 + dy
        bx = x2 + dx
        by = y2 + dy
        a_cand.append((ax, ay))
        b_cand.append((bx, by))
ans = "No"
for a in a_cand:
    for b in b_cand:
        if a == b:
            ans = 'Yes'
print(ans)
