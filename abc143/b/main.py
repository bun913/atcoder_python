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

# Nが最大で50
N = int(input())
D = list(map(int, input().split()))
com_list = list(combinations([i for i in range(N)], 2))

ans = 0
for i, j in com_list:
    x = D[i]
    y = D[j]
    ans += x * y
print(ans)
