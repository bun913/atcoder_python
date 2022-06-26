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

N, X = list(map(int, input().split()))

s = ''
for i in range(97, 123):
    lower = chr(i)
    upp = lower.upper()
    s += upp * N
print(s[X-1])
