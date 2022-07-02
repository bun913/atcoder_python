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

N = int(input())

memo = {}


def calc_s(n: int):
    # メモ化再起にしてみたバージョン
    if n in memo:
        return memo[n]
    if n == 1:
        return [1]
    return calc_s(n-1) + [n] + calc_s(n-1)


S = calc_s(N)
print(*S)
