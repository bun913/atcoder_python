# -*- coding: utf-8 -*-
"""
N種類の魔法が使えて、i番目の魔法を使うと、体力をAi減らすことができる
魔力はBiを消費する
モンスターを倒すために必要な魔力の最小値を求める
同じ魔法は何度でも使うことができる
貪欲法では無理そう。DPで解けると思う。
Hはたかだかが10**4なので、HPを横軸に取ろう
"""
H, N = map(int, input().split())
A = []
B = []
for _ in range(N):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)

# DP表の作成と初期化
dp = [10**10 for _ in range(H+1)]
dp[0] = 0

for i in range(N):
    a = A[i]
    b = B[i]
    for h in range(H+1):
        # ダメージがHPを上回らない場合
        if h+a <= H:
            dp[h+a] = min(dp[h+a], dp[h]+b)
            continue
        dp[H] = min(dp[H], dp[h]+b)
print(dp[-1])
