# -*- coding: utf-8 -*-
"""
Atcoderの問題解く用

全ての組み合わせを列挙する方法
list(0...8)から2つを抜き出す
list(combinations(l, 2))

bit全探索でフラグが立っているかチェックする
if ((i >> j) & 1)
"""
L = list(map(int, input().split()))
S = list(set(L))
if len(S) != 2:
    print('No')
    exit()
a = S[0]
b = S[1]

if (L.count(a) == 3 and L.count(b) == 2) or (L.count(a) == 2 and L.count(b) == 3):
    print('Yes')
    exit()
print('No')
