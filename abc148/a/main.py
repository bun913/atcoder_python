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

A = int(input())
B = int(input())
s = set([A, B])
all_set = set([1, 2, 3])

dif = all_set.difference(s)
print(list(dif)[0])
