# -*- coding: utf-8 -*-
"""
Atcoderの問題解く用

全ての組み合わせを列挙する方法
list(0...8)から2つを抜き出す
list(combinations(l, 2))

bit全探索でフラグが立っているかチェックする
if ((i >> j) & 1)
"""
from functools import reduce, lru_cache
from itertools import combinations
from math import radians, sqrt, cos, sin
import numpy as np


def cosine_theorem(a, b, angle):
    '''
    予言定理
    aとbという三角形の2辺とその間の角度から3辺目の長さがわかる
    '''
    rad = radians(angle)
    _cos = cos(rad)
    c_square = (a ** 2) - (2 * a * b * _cos) + (b ** 2)
    c = sqrt(c_square)
    return c


def rotation_matrix(x, y, angle):
    rad = radians(d)
    ans = (a * cos(rad) - b * sin(rad), a * sin(rad) + b * cos(rad))
    return ans

# ある点から反時計回りに回転させる方ほとして回転行列を使う
# 回転行列をライブラリ化しておく


a, b, d = list(map(int, input().split()))
ans = rotation_matrix(a, b, d)
print(ans[0], ans[1])
