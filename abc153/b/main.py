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

H, N = list(map(int, input().split()))
A = list(map(int, input().split()))
s = sum(A)

if s >= H:
    print('Yes')
    exit()
print('No')
