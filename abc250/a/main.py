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
R, C = list(map(int, input().split()))

ans = 0
for i in range(H):
    for j in range(W):
        is_ok = abs(i+1-R) + abs(j+1-C) == 1
        if is_ok:
            ans += 1
print(ans)
