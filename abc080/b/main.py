# -*- coding: utf-8 -*-
"""
Atcoderの問題解く用

全ての組み合わせを列挙する方法
list(0...8)から2つを抜き出す
list(combinations(l, 2))

bit全探索でフラグが立っているかチェックする
if ((i >> j) & 1)
"""


def f(n: int):
    L = list(str(n))
    L = list(map(int, L))
    return sum(L)


N = int(input())
calced = f(N)
if N % calced == 0:
    print('Yes')
    exit()
print('No')
