# -*- coding: utf-8 -*-
"""
Atcoderの問題解く用

全ての組み合わせを列挙する方法
list(0...8)から2つを抜き出す
list(combinations(l, 2))

bit全探索でフラグが立っているかチェックする
if ((i >> j) & 1)
"""
D, N = list(map(int, input().split()))

if D == 0:
    ans = N
    if N == 100:
        ans = 101
    print(ans)
    exit()

if D == 1:
    ans = 100 * N
    if N == 100:
        ans = 101 * 100
    print(ans)
    exit()

if D == 2:
    ans = 10000 * N
    if N == 100:
        ans = 10000 * 101
    print(ans)
    exit()
