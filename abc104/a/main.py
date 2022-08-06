# -*- coding: utf-8 -*-
"""
Atcoderの問題解く用

全ての組み合わせを列挙する方法
list(0...8)から2つを抜き出す
list(combinations(l, 2))

bit全探索でフラグが立っているかチェックする
if ((i >> j) & 1)
"""
R = int(input())

if R < 1200:
    print('ABC')
    exit()
if R < 2800:
    print('ARC')
    exit()
print('AGC')
