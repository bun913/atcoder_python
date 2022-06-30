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

N, A, B = list(map(int, input().split()))
# 最終的な青いボールの個数を調べれば良い
# 列の先頭からN個のうち青が何個か調べる
pair = A + B
set_num = N // pair
rest = N % pair

ans = A * set_num
ans += min(rest, A)

print(ans)
