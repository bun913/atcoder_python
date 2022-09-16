# -*- coding: utf-8 -*-
"""
Atcoderの問題解く用

全ての組み合わせを列挙する方法
list(0...8)から2つを抜き出す
list(combinations(l, 2))

bit全探索でフラグが立っているかチェックする
if ((i >> j) & 1)
"""
from itertools import product

N = int(input())

elms = ["a", "b", "c"]

itels = [elms for _ in range(N)]

for s in product(*itels):
    print("".join(s))
