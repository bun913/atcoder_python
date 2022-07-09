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
import math

S = input()
R = S[::-1]


cnt = 0
for i in range(len(S)):
    s = S[i]
    r = R[i]
    if s != r:
        cnt += 1
print(cnt // 2)
