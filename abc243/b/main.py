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
A = list(map(int, input().split()))
B = list(map(int, input().split()))

eq = 0
dif = 0
for i in range(N):
    for j in range(N):
        if A[i] == B[j]:
            if i == j:
                eq += 1
            else:
                dif += 1
print(eq)
print(dif)
