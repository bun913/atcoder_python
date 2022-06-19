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

N, K = list(map(int, input().split()))
A = list(map(int, input().split()))
B = list(map(int, input().split()))


_max = max(A)
ans = 'No'
for i in range(N):
    a = A[i]
    if a == _max and i+1 in B:
        ans = 'Yes'
        break
print(ans)
