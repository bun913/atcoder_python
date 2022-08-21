# -*- coding: utf-8 -*-
"""
Atcoderの問題解く用

全ての組み合わせを列挙する方法
list(0...8)から2つを抜き出す
list(combinations(l, 2))

bit全探索でフラグが立っているかチェックする
if ((i >> j) & 1)
"""
X, Y, N = list(map(int, input().split()))
cand1 = N * X

rest = N % 3
cand2 = (N // 3) * Y + rest * X
ans = min(cand1, cand2)
print(ans)
