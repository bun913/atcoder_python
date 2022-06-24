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

A, B, C, D = list(map(int, input().split()))

ans = 'No'

while True:
    C -= B
    # 高橋の攻撃で青木が沈む
    if C <= 0:
        ans = 'Yes'
        break
    # 青木の攻撃で高橋が沈む
    A -= D
    if A <= 0:
        break
print(ans)
