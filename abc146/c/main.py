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

"""
考えたこと
二部探索でいけばlogの計算で間に合うのでは？
"""

A, B, X = list(map(int, input().split()))

# 2分探
# 一番小さいのはまず0から
# 最初に考えられる右端は10**9+1としておく
l = 0
r = 10 ** 9 + 1
while r - l > 1:
    c = (l + r) // 2
    calced = A * c + B * len(str(c))
    if calced <= X:
        l = c
    else:
        r = c
print(l)
