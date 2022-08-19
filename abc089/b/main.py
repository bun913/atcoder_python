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
S = list(input().split())
ans_set = set(S)
if len(ans_set) == 3:
    print('Three')
    exit()
print('Four')
