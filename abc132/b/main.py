# -*- coding: utf-8 -*-
"""
Atcoderの問題解く用

全ての組み合わせを列挙する方法
list(0...8)から2つを抜き出す
list(combinations(l, 2))

bit全探索でフラグが立っているかチェックする
if ((i >> j) & 1)
"""

n = int(input())
P = list(map(int, input().split()))

ans = 0

for i in range(1, n-1):
    bef = P[i-1]
    cur = P[i]
    aft = P[i+1]
    if sorted([bef, cur, aft])[1] == cur:
        ans += 1
print(ans)
