# -*- coding: utf-8 -*-
"""
Atcoderの問題解く用

全ての組み合わせを列挙する方法
list(0...8)から2つを抜き出す
list(combinations(l, 2))

bit全探索でフラグが立っているかチェックする
if ((i >> j) & 1)
"""
from functools import reduce, lru_cache
from itertools import combinations
import math

# 偶数の数字が3か5で割り切れるかどうか
ans = 'APPROVED'
N = int(input())
A = list(map(int, input().split()))

for a in A:
    if a % 2 != 0:
        continue
    if a % 3 == 0 or a % 5 ==0:
        continue
    print('DENIED')
    exit()

print(ans)
