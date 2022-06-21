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

N = input()
s = int(N[-1])

if s in [2, 4, 5, 7, 9]:
    print('hon')
elif s in [0, 1, 6, 8]:
    print('pon')
else:
    print('bon')
