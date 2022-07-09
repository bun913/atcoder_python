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

N, M, X, T, D = list(map(int, input().split()))
ans = T
for a in range(M, N+1):
    if 0 <= a and a < X:
        ans -= D
print(ans)
