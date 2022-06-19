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

N, A, B = list(map(int, input().split()))
# N * N のここのタイルがある
tiles = []
for i in range(N * A):
    row = []
    for j in range(N * B):
        a = (i // A)
        b = (j // B)
        if (a+b) % 2 == 0:
            row.append('.')
        else:
            row.append('#')
    print(*row, sep="")
