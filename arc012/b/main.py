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

N, va, vb, L = list(map(int, input().split()))

target = L
ans = 0
taka = 0
for i in range(N):
    second = (target-taka) / va
    target += (second) * vb
    taka += va * second
    # print('target:', target, 'taka:', taka)
ans = target-taka
if ans < 0:
    print(0)
else:
    print(ans)
