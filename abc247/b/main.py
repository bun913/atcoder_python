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
memo = {}
l = []
# 性別の辞書と性別のタプルを作っておく
for _ in range(N):
    s, t = input().split(' ')
    l.append((s, t))
    if s in memo:
        memo[s] += 1
    else:
        memo[s] = 1
    if t in memo:
        memo[t] += 1
    else:
        memo[t] = 1

ans = 'Yes'

for st in l:
    result = []
    for v in st:
        if memo[v] >= 2:
            result.append(False)
        else:
            result.append(True)
    if result[0] is False and result[1] is False:
        print('No')
        exit()
print(ans)
