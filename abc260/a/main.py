# -*- coding: utf-8 -*-
"""
Atcoderの問題解く用

全ての組み合わせを列挙する方法
list(0...8)から2つを抜き出す
list(combinations(l, 2))

bit全探索でフラグが立っているかチェックする
if ((i >> j) & 1)
"""
import itertools

S = input()
s = sorted(S)
grouped = [(k, list(g)) for k, g in itertools.groupby(s)]

ans = -1
for k, v in grouped:
    if len(v) == 1:
        print(v[0])
        exit()
print(ans)
