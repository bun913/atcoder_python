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
P = 0
# 大きめのlistを用意してはみ出した文をポイントにする
B = [0 for _ in range(8)]
B[0] = 1

for i in range(N):
    a = A[i]
    B[0] = 1
    for j in range(3, -1, -1):
        if B[j] == 1:
            B[j+a] = 1
            B[j] = 0
    # ４以上は足し上げて0に戻す
    P += sum(B[4:])
    B[4:] = [0, 0, 0, 0]

print(P)
