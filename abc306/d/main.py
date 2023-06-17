# -*- coding: utf-8 -*-
"""
"""
N = int(input())
X = []
Y = []
for _ in range(N):
    x, y = map(int, input().split())
    X.append(x)
    Y.append(y)

# dp[i][0]: i番目の料理まで食べたときに、お腹を壊していない状態でのおいしさの最大値
# dp[i][1]: i番目の料理まで食べたときに、お腹を壊している状態でのおいしさの最大値
dp = [[-float('inf'), -float('inf')] for _ in range(N+1)]
dp[0][0] = 0
dp[0][1] = 0

for i in range(1, N+1):
    # i番目の料理を食べない場合
    dp[i][0] = max(dp[i][0], dp[i-1][0])
    dp[i][1] = max(dp[i][1], dp[i-1][1])
    # i番目の料理を食べる場合
    if X[i-1] == 0:
        # 解毒剤入りの場合
        dp[i][0] = max([dp[i][0], dp[i-1][1] + Y[i-1], dp[i-1][0] + Y[i-1]])
    else:
        # 毒入りの場合
        dp[i][1] = max([dp[i][1], dp[i-1][0] + Y[i-1]])
print(max(dp[N]))
