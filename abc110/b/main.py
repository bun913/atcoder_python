# -*- coding: utf-8 -*-
"""
Atcoderの問題解く用

全ての組み合わせを列挙する方法
list(0...8)から2つを抜き出す
list(combinations(l, 2))

bit全探索でフラグが立っているかチェックする
if ((i >> j) & 1)
"""
N, M, X, Y = list(map(int, input().split()))
xl = list(map(int, input().split()))
yl = list(map(int, input().split()))

for Z in range(X+1, Y+1):
    filterd_xl = [i for i in xl if i < Z]
    filterd_yl = [i for i in yl if i >= Z]
    if len(filterd_xl) == len(xl) and len(filterd_yl) == len(yl):
        print('No War')
        exit()
print('War')
