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
T, A = list(map(int, input().split()))
H = list(map(int, input().split()))

ans = 0
abs_min = float('inf')

for i in range(N):
    h = H[i]
    ave = T - (h * 6 / 1000)
    ab = abs(A-ave)
    if ab == min(abs_min, ab):
        abs_min = ab
        ans = i + 1
print(ans)
