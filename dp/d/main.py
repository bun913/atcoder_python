# -*- coding: utf-8 -*-
"""
いわゆるナップサック問題だ！
2次元の表で価値の総和を保持していけばわかる
"""
N, W = map(int, input().split())
weights = []
values = []
for _ in range(N):
    w, v = map(int, input().split())
    weights.append(w)
    values.append(v)
# i個までの品物を使って重さがW以下になるように選べる価値の総和の最大値を求める
dp = [[0 for _ in range(W+1)] for _ in range(N+1)]

for i in range(1, N+1):
    w = weights[i-1]
    v = values[i-1]
    for j in range(W+1):
        # i番目の品物を使わない場合の価値の最大値
        cand1 = dp[i-1][j]
        dp[i][j] = cand1
        if j < w:
            continue
        # i番目の品物を使う場合の価値の最大値
        cand2 = dp[i-1][j-w] + v
        dp[i][j] = max(cand1, cand2)
print(dp[-1][-1])
