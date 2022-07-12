# -*- coding: utf-8 -*-
"""
Atcoderの問題解く用

全ての組み合わせを列挙する方法
list(0...8)から2つを抜き出す
list(combinations(l, 2))

bit全探索でフラグが立っているかチェックする
if ((i >> j) & 1)
"""

N = int(input())

for i in range(1, 10):
    for j in range(1, 10):
        if i * j == N:
            print('Yes')
            exit()
print('No')
