# -*- coding: utf-8 -*-
"""
Atcoderの問題解く用

全ての組み合わせを列挙する方法
list(0...8)から2つを抜き出す
list(combinations(l, 2))

bit全探索でフラグが立っているかチェックする
if ((i >> j) & 1)
"""
n, k = map(int, input().split())
P = list(map(int, input().split()))

ans = 0
cnt = 0
for right in range(n):
    ans += (P[right] + 1) / 2
    if right - k >= 0:
        ans -= (P[right - k] + 1) / 2
    cnt = max(cnt, ans)

print(cnt)
