# -*- coding: utf-8 -*-
"""
Atcoderの問題解く用

全ての組み合わせを列挙する方法
list(0...8)から2つを抜き出す
list(combinations(l, 2))

bit全探索でフラグが立っているかチェックする
if ((i >> j) & 1)
"""
a, b, c, d = list(map(int, input().split()))

if abs(a-c) <= d:
    print('Yes')
    exit()
if abs(a-b) <= d and abs(b-c) <= d:
    print('Yes')
    exit()
print('No')
