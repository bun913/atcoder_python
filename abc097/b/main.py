# -*- coding: utf-8 -*-
"""
Atcoderの問題解く用

全ての組み合わせを列挙する方法
list(0...8)から2つを抜き出す
list(combinations(l, 2))

bit全探索でフラグが立っているかチェックする
if ((i >> j) & 1)
"""
from math import sqrt

X = int(input())

ans = -1
for b in range(1, X+1):
    if b == 1:
        ans = max(ans, 1)
        continue
    p = 2
    while b ** p <= X:
        ans = max(b ** p, ans)
        p += 1
print(ans)
