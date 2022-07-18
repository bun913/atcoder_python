# -*- coding: utf-8 -*-
"""
Atcoderの問題解く用

全ての組み合わせを列挙する方法
list(0...8)から2つを抜き出す
list(combinations(l, 2))

bit全探索でフラグが立っているかチェックする
if ((i >> j) & 1)
"""

# Nが10 ** 5 なのでループで求めるか

N = int(input())

ans = 0

for n in range(1, N+1):
    le = len(str(n))
    if le % 2 != 0:
        ans += 1
print(ans)
