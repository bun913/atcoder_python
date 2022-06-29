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

S = input()
N = len(S)

cond1 = S == S[::-1]
ind1 = ((N-1) // (2) - 1)
cond2 = S[:ind1+1] == S[:ind1+1][::-1]
ind2 = ((N+3) // (2) - 1)
cond3 = S[ind2:N] == S[ind2:N][::-1]

ans = 'No'

all_cond = all([cond1, cond2, cond3])
# print([cond1, cond2, cond3])
if all_cond is True:
    ans = 'Yes'
print(ans)
