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

# 与えられるのは純烈
# 任意の整数jに対して、Pi < Pjとなるものの個数
# でもNが2 * 10 **5 なので何も考えずに2重ループはできない
# 問題を見ると自分より大きな数字がなければ良さそう

_min = float('inf')
N = int(input())
P = list(map(int, input().split()))
ans = 0

for p in P:
    if min(_min, p) == p:
        ans += 1
    _min = min(_min, p)
print(ans)
