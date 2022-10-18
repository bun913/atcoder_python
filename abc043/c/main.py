# -*- coding: utf-8 -*-
"""
答えの値から離れ場離れるほどコストは大きくなる
普通に答えの幅が小さいので全探索で間に合いそう
"""
N = int(input())
A = list(map(int, input().split()))
ad = sorted(A)

ans = float("inf")
for n in range(-100, 101):
    s = 0
    for a in ad:
        s += (a - n) ** 2
    ans = min(ans, s)

print(ans)
