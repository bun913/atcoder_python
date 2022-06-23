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

a, b, c = [int(input()) for _ in range(3)]

l = sorted([a, b, c], reverse=True)
l = list(map(str, l))
for n in [a, b, c]:
    i = l.index(str(n))
    print(i+1)
