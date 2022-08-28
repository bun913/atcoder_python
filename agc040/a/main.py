# -*- coding: utf-8 -*-
"""
Atcoderの問題解く用

全ての組み合わせを列挙する方法
list(0...8)から2つを抜き出す
list(combinations(l, 2))

bit全探索でフラグが立っているかチェックする
if ((i >> j) & 1)
"""
S = input()
n = len(S) + 1
A = [0 for _ in range(len(S)+1)]

for i in range(n-1):
    if S[i] == '<':
        A[i+1] = max(A[i+1], A[i]+1)
for i in range(n-2, -1, -1):
    if S[i] == '>':
        A[i] = max(A[i], A[i+1]+1)
print(sum(A))
