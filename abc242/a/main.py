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

A, B, C, X = list(map(int, input().split()))
if X <= A:
    print(1.0)
    exit()
elif A+1 <= X and X <= B:
    mon = (B-A+1) - 1
    print(C / mon)
    exit()
else:
    print(0.0)
