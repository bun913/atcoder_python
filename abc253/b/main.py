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
a = []
b = []
for i in range(H):
    s = list(input())
    for j in range(W):
        if s[j] == 'o':
            # aにすでに入っている場合はbに入れる
            if len(a) > 0:
                b.append(i)
                b.append(j)
            else:
                a.append(i)
                a.append(j)
print(abs(a[0]-b[0]) + abs(a[1] - b[1]))
