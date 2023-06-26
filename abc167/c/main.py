# -*- coding: utf-8 -*-
"""
N,Mが非常に小さいのでbit全探索で利用する参考書を選べる
"""
from itertools import product

N, M, X = map(int, input().split())
C = []
A = []
for i in range(N):
    c, *a = map(int, input().split())
    C.append(c)
    A.append(a)

ans = 10**15
for bools in product([True, False], repeat=N):
    unds = [0] * M
    cost = 0
    for i, is_use in enumerate(bools):
        if is_use is False:
            continue
        for j, a in enumerate(A[i]):
            unds[j] += a
        cost += C[i]
    if all([und >= X for und in unds]):
        ans = min(ans, cost)
if ans == 10**15:
    print(-1)
    exit()
print(ans)
