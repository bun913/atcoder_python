# -*- coding: utf-8 -*-
"""
解く前のメモ

一番西の旅館は海を眺められ、それ以降の旅館は自分がこれまでの旅館の中で最高の高さの場合にだけ眺められる
"""

N = int(input())
H = list(map(int, input().split()))

_max = H[0]
ans = 1

for i in range(1, N):
    h = H[i]
    if h >= _max:
        ans += 1
    _max = max(_max, h)
print(ans)
