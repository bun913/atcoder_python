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

a, b = list(map(int, input().split()))
ad, bd = (a % 10, b % 10)

ans = 'No'
if abs(ad - bd) == 1:
    ans = 'Yes'
elif a == 9 and b == 10:
    ans = 'Yes'
print(ans)
