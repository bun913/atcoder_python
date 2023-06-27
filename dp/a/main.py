# -*- coding: utf-8 -*-
"""
まさにDPですというお手本問題
1次元配列でh[i]の足場までの最適解を保持することを繰り返す
"""
N = int(input())
H = list(map(int, input().split()))
dp = [float('inf')] * N
dp[0] = 0
dp[1] = abs(H[1] - H[0])
for i in range(N):
    if i <= 1:
        continue
    cand1 = dp[i-1] + abs(H[i] - H[i-1])
    cand2 = dp[i-2] + abs(H[i] - H[i-2])
    dp[i] = min(cand1, cand2)
print(dp[-1])
