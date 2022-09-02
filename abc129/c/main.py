# -*- coding: utf-8 -*-
"""
Nまで辿り着ける移動方法は何通りか
"""
N, M = list(map(int, input().split()))
A = set()
[A.add(int(input())) for _ in range(M)]

DP = [1] + list(range(N))
mod = 1000000007

for i in range(1, N + 1):
    if i in A:
        DP[i] = 0
        continue
    # 1段前
    cur = 0
    if (i - 1) not in A and DP[i - 1] != 0:
        cur = DP[i - 1]
    # 2段前からも来れる
    if (i - 2) >= 0 and (i - 2) not in A and DP[i - 2] != 0:
        cur += DP[i - 2]
    DP[i] = cur % mod
print(DP[-1] % mod)
