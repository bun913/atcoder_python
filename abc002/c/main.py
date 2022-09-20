# -*- coding: utf-8 -*-
"""
Atcoderの問題解く用

全ての組み合わせを列挙する方法
list(0...8)から2つを抜き出す
list(combinations(l, 2))

bit全探索でフラグが立っているかチェックする
if ((i >> j) & 1)
"""
import numpy as np

xa, ya, xb, yb, xc, yc = list(map(int, input().split()))
vec1 = np.array([xa, ya]) - np.array([xb, yb])
vec2 = np.array([xa, ya]) - np.array([xc, yc])
ans = np.cross(vec1, vec2) / 2
print(abs(ans))
