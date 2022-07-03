# -*- coding: utf-8 -*-
"""
Atcoderの問題解く用

全ての組み合わせを列挙する方法
list(0...8)から2つを抜き出す
list(combinations(l, 2))

bit全探索でフラグが立っているかチェックする
if ((i >> j) & 1)
"""
from functools import reduce, lru_cache
from itertools import combinations
import math

S, T = input().split()
A, B = list(map(int, input().split()))
U = input()

if U == S:
    A -= 1
if U == T:
    B -= 1
print(A, B)
