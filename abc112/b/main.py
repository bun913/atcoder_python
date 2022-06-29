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

N, T = list(map(int, input().split()))
ans = 2000

for i in range(N):
    c, t = list(map(int, input().split()))
    if t > T:
        continue
    ans = min(c, ans)
if ans == 2000:
    ans = 'TLE'
print(ans)
