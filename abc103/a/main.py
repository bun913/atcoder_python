# -*- coding: utf-8 -*-
"""
Atcoderの問題解く用

全ての組み合わせを列挙する方法
list(0...8)から2つを抜き出す
list(combinations(l, 2))

bit全探索でフラグが立っているかチェックする
if ((i >> j) & 1)
"""

A = list(map(int, input().split()))
S = sorted(A)

ans = 0
for i in range(3):
    if i == 0:
        continue
    cost = abs(S[i] - S[i-1])
    ans += cost
print(ans)
