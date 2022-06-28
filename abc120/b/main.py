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

A, B, K = list(map(int, input().split()))

ks = []

for i in range(1, max(A, B)+1):
    if A % i == 0 and B % i == 0:
        ks.append(i)
print(sorted(ks, reverse=True)[K-1])
