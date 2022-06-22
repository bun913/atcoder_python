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

N, K = list(map(int, input().split()))
have = set()
every = set([i for i in range(1, N+1)])

for i in range(K):
    _d = int(input())
    l = list(map(int, input().split()))
    for a in l:
        have.add(a)
ans = every.difference(have)

print(len(ans))
