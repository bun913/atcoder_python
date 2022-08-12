# -*- coding: utf-8 -*-
"""
Atcoderの問題解く用

全ての組み合わせを列挙する方法
list(0...8)から2つを抜き出す
list(combinations(l, 2))

bit全探索でフラグが立っているかチェックする
if ((i >> j) & 1)
"""
A, B, C, D = list(map(int, input().split()))
L = A + B
R = C + D
ans = 'Left'
if L < R:
    ans = 'Right'
elif L == R:
    ans = 'Balanced'
print(ans)
