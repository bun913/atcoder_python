# -*- coding: utf-8 -*-
"""
Atcoderの問題解く用

全ての組み合わせを列挙する方法
list(0...8)から2つを抜き出す
list(combinations(l, 2))

bit全探索でフラグが立っているかチェックする
if ((i >> j) & 1)
"""
Y = int(input())
mod = Y % 4
if mod == 2:
    print(Y)
    exit()
if mod == 0:
    print(Y+2)
    exit()
if mod == 1:
    print(Y+1)
    exit()
if mod == 3:
    print(Y+3)
    exit()
