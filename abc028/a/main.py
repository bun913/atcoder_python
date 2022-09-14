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

if N <= 59:
    print("Bad")
elif N <= 89:
    print("Good")
elif N <= 99:
    print("Great")
else:
    print("Perfect")
