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
T = input()

x, y = 0, 0
dr = 'E'

for i in range(N):
    t = T[i]
    if t == 'R':
        if dr == 'E':
            dr = 'S'
        elif dr == 'S':
            dr = 'W'
        elif dr == 'W':
            dr = 'N'
        elif dr == 'N':
            dr = 'E'
    else:
        if dr == 'E':
            x += 1
        elif dr == 'W':
            x -= 1
        elif dr == 'N':
            y += 1
        else:
            y -= 1
print('{} {}'.format(x, y))
