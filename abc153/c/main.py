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

N, K = list(map(int, input().split()))
H = list(map(int, input().split()))

# 必殺技を全員に使える
if K >= N:
    print(0)
    exit()
_sorted = sorted(H, reverse=True)
# 体力が大きい順に技を使う
ans = sum(_sorted[K:])
print(ans)
