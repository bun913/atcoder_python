"""
N個のサイコロがある
i番ん目のサイコロはpiまでの種類の目がそれぞれ等確率ででる
出る目の合計の期待値の最大値を求める
期待値をあらかじめ求めておく必要がありそう
この期待値は基本的に前の結果からあらかじめ求めることができる
piは最大で1000なので求めておく
"""
N, K = map(int, input().split())
P = list(map(int, input().split()))
# 累積和から期待値を求めておく
S = [0] * 1001
E = [0] * 1001
S[1] = 1
E[1] = 1
for i in range(2, 1000+1):
    S[i] = S[i-1] + i
    E[i] = S[i] / i
# Pから各区間の累積和を算出する
acc = [0] * (N+1)
for i in range(1, N+1):
    acc[i] = acc[i-1] + E[P[i-1]]
# 最大の区間和を求める
ans = 0
for i in range(N-K+1):
    ans = max(ans, acc[i+K] - acc[i])
print(ans)
