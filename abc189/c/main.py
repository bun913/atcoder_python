# -*- coding: utf-8 -*-
"""
"""
N = int(input())
A = list(map(int, input().split()))

ans = -10**15
for l in range(N):
    mina = A[l]
    for r in range(l, N):
        mina = min(mina, A[r])
        ans = max(ans, mina * (r-l + 1))
print(ans)
