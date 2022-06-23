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
from decimal import Decimal

A = Decimal(input())
B = Decimal(input())

if A > B:
    print('GREATER')
elif A < B:
    print('LESS')
else:
    print('EQUAL')
