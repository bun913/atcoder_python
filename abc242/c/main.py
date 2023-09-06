# -*- coding: utf-8 -*-
"""
"""

N = int(input())
dp = [[0 for _ in range(9)] for _ in range(N)]
mod = 998244353
# dpのわかるところから埋める
# dp[1]の行は全部1になる
for i in range(9):
    dp[0][i] = 1

for i in range(N):
    if i == 0:
        continue
    for j in range(9):
        left_up = dp[i-1][j-1] if j-1 >= 0 else 0
        up = dp[i-1][j]
        right_up = dp[i-1][j+1] if j+1 <= 8 else 0
        cur = (left_up + up + right_up) % mod
        dp[i][j] = cur
print(sum(dp[-1]) % mod)
