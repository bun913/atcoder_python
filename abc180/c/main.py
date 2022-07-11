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

# 約数列挙の問題
# Nが10 ** 12なので全部列挙は間に合わない
# 約数は平方根まで計算すれば十分である性質を利用すれば余裕

N = int(input())
sqr = math.sqrt(N)
divs = set()

for i in range(1, int(sqr) + 1):
    if N % i == 0:
        divs.add(i)
        divs.add(N // i)

ans_list = sorted(list(divs))
print(*ans_list, sep="\n")
