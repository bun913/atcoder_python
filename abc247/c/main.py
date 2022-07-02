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

# Nはたかだか16でたかだか65,536文字にしかならないから全部一から計算しても問題なさそう

N = int(input())


def calc_s(n: int):
    if n == 1:
        return [1]
    return calc_s(n-1) + [n] + calc_s(n-1)


S = calc_s(N)
print(*S)
