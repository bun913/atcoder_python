# -*- coding: utf-8 -*-
"""
Atcoderの問題解く用

全ての組み合わせを列挙する方法
list(0...8)から2つを抜き出す
list(combinations(l, 2))

bit全探索でフラグが立っているかチェックする
if ((i >> j) & 1)
"""
H, W = list(map(int, input().split()))
h, w = list(map(int, input().split()))

al = H * W
rem = (h * W) + (w * H) - (h * w)

ans = al - rem
print(ans)
