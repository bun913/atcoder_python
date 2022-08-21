# -*- coding: utf-8 -*-
"""
Atcoderの問題解く用

全ての組み合わせを列挙する方法
list(0...8)から2つを抜き出す
list(combinations(l, 2))

bit全探索でフラグが立っているかチェックする
if ((i >> j) & 1)
"""
N, M, T = list(map(int, input().split()))
A = list(map(int, input().split()))
bonus = {}
for _ in range(M):
    x, y = list(map(int, input().split()))
    bonus[x] = y

rest = T
for i in range(N-1):
    n = i + 1
    if n in bonus:
        rest += bonus[n]
    a = A[i]
    if rest - a <= 0:
        print('No')
        exit()
    rest -= a
print('Yes')
