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

A, B = list(map(int, input().split()))
# 何階分の階段を上必要があるか
# 地下1回の上は1回(0階がない)

if A > 0 and B > 0:
    print(B-A)
if A < 0 and B > 0:
    print(B-A-1)
if A < 0 and B < 0:
    print(B-A)
