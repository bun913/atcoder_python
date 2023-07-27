# -*- coding: utf-8 -*-
"""
長さNの数列であって
Ai全てが1以上M以下かつAの総和がK以下である数列の個数をもとめる
"""
N, M, K = map(int, input().split())
mod = 998244353
dp = [[0] * (K+1) for _ in range(N+1)]
# 1行目(長さ1の数列)の初期化(1以上M以下の数は1通り作れる)
for a in range(1, M+1):
    dp[1][a] = 1

for i in range(2, N+1):
    for x in range(1, K+1):
        # j= 1 ~ (x-1)までの列挙
        for j in range(1, x):
            # M以下の数しか数列に使えないので、x-jがM以下の場合のみ足す
            if x-j <= M:
                dp[i][x] += dp[i-1][j]
                dp[i][x] %= mod
ans = 0

for x in range(1, K+1):
    ans += dp[N][x]
    ans %= mod
print(ans)
