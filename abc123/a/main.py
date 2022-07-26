# -*- coding: utf-8 -*-
"""
Atcoderの問題解く用

全ての組み合わせを列挙する方法
list(0...8)から2つを抜き出す
list(combinations(l, 2))

bit全探索でフラグが立っているかチェックする
if ((i >> j) & 1)
"""
A = [int(input()) for _ in range(5)]
k = int(input())

ans = 'Yay!'

for i in range(5):
    for j in range(i+1, 5):
        x = A[i]
        y = A[j]
        if abs(x-y) > k:
            ans = ':('
            break
print(ans)
