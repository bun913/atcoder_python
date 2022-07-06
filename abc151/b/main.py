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

N, K, M = list(map(int, input().split()))
A = list(map(int, input().split()))
s = sum(A)

ans = -1

for i in range(K+1):
    _sum = s + i
    avg = _sum / N
    if avg >= M:
        ans = i
        break
print(ans)
