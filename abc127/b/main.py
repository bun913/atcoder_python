# -*- coding: utf-8 -*-
"""
Atcoderの問題解く用

全ての組み合わせを列挙する方法
list(0...8)から2つを抜き出す
list(combinations(l, 2))

bit全探索でフラグが立っているかチェックする
if ((i >> j) & 1)
"""
r, D, x2000 = list(map(int, input().split()))


def calc(x: int, r, D):
    if x == 2000:
        return x2000
    return r * (calc(x-1, r, D)) - D


for x in range(2001, 2011):
    print(calc(x, r, D))
