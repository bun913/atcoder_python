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
B = list(map(int, input().split()))
C = list(map(int, input().split()))

s = 0
bef = -1

for i in range(N):
    a = A[i]
    b = B[a-1]
    s += b
    if i == 0:
        bef = a
        continue
    # 満足度を満たす場合
    if bef + 1 == a:
        extra = C[bef-1]
        s += extra
    bef = a
print(s)
