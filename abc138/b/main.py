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
A = list(map(int, input().split()))

r_sum = 0

for i in range(N):
    a = A[i]
    r_sum += (1/a)
print(1/r_sum)
