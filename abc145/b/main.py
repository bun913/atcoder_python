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
if N % 2 != 0:
    print("No")
    exit()
S = input()
left = S[:N//2]
right = S[N//2:]

ans = 'No'
if left == right:
    ans = 'Yes'
print(ans)
