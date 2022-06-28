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

X = int(input())
yen500 = X // 500
yen5 = 0
rest = X - (yen500 * 500)

if rest > 0:
    yen5 = rest // 5
print((yen500 * 1000) + yen5 * 5)
