# -*- coding: utf-8 -*-
"""
Atcoderの問題解く用

全ての組み合わせを列挙する方法
list(0...8)から2つを抜き出す
list(combinations(l, 2))

bit全探索でフラグが立っているかチェックする
if ((i >> j) & 1)
"""
K = int(input())
even = K // 2
odd = K // 2
if K % 2 != 0:
    odd += 1

ans = even * odd

print(ans)
