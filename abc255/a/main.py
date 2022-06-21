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

r, c = list(map(int, input().split()))
A = [list(map(int, input().split())) for _ in range(2)]

print(A[r-1][c-1])
