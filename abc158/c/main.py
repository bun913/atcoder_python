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

A, B = list(map(int, input().split()))

# A,Bが100以下なので、せいぜいxは100倍くらいまでなのでそれを全探索する

for i in range(min(A, B), 10000):
    a = i * 8 // 100
    b = i * 10 // 100
    if (a == A) and (b == B):
        print(i)
        exit()
print(-1)
