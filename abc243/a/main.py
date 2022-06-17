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

v, a, b, c = list(map(int, input().split()))
l = [a, b, c]
i = 0
while True:
    h = l[i]
    if v - h < 0:
        if i == 0:
            print('F')
        elif i == 1:
            print('M')
        else:
            print('T')
        exit()
    v -= h
    if i == 2:
        i = 0
    else:
        i += 1
