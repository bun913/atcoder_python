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
from itertools import combinations, chain
import math

# 普通にforだと面白くないのでzipを使ってみよう
N = int(input())
S, T = input().split(' ')
s = list(S)
t = list(T)

zipped = zip(s, t)
flatten = list(chain.from_iterable(zipped))
print(*flatten, sep='')
