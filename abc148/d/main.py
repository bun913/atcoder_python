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

# Nが最大200,000なのでループは1回はできる
# 単純に最後に[1,2,3...]と初項1,差分1の等差数列になればOK

N = int(input())
A = list(map(int, input().split()))
B = A[:]

_next = 1
ans = 0

for i in range(N):
    a = A[i]
    if a != _next:
        # 要素を実際に抜くと面倒なため-1を砕いた印とする
        B[i] = -1
        ans += 1
        continue
    _next += 1

expcted = 1
removed = [b for b in B if b != -1]

# -1しかなかった場合
if len(removed) == 0:
    print(-1)
    exit()

for b in removed:
    if expcted == b:
        expcted += 1
        continue
    # 等差数列じゃなかった
    print(-1)
    exit()
print(ans)
