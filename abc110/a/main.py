# -*- coding: utf-8 -*-
"""
Atcoderの問題解く用

全ての組み合わせを列挙する方法
list(0...8)から2つを抜き出す
list(combinations(l, 2))

bit全探索でフラグが立っているかチェックする
if ((i >> j) & 1)
"""
a, b, c = list(map(int, input().split()))
cand1 = a * 10 + b + c
cand2 = b * 10 + c + a
cand3 = c * 10 + a + b

print(max([cand1, cand2, cand3]))
