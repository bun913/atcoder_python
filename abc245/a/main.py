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

a, b, c, d = list(map(int, input().split()))
ta = a + (b / 60)
ao = c + (d / 60) + 1 / 3600
if ta < ao:
    print('Takahashi')
else:
    print('Aoki')
