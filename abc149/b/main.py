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

# A >=1 a--
# B >=1 b--
# 10**12あるのでKはループできない

A, B, K = list(map(int, input().split()))
# 高橋のか食べる
if A >= K:
    print(A-K, B)
    exit()
# 青木のを食べる
if B >= (K-A):
    print(0, B-(K-A))
    exit()
print(0, 0)
