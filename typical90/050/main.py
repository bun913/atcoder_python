# -*- coding: utf-8 -*-
"""
解く前のメモ

N段を1歩、またはLずつ登れる
移動方法が何通りあるか 10**9 + 7で割ったあまりを求める

以下解説AC
数学的にパッとわからない問題なら、一旦DPで考えてみるのが良いかも
1段を積むか、L段を積むかっていう問題なら積み上げていくだけだし
"""
N, L = list(map(int, input().split()))
DP = [0 for _ in range(N+1)]
DP[0] = 1
mod = 10 ** 9 + 7

for i in range(1, N+1):
    if i < L:
        DP[i] = 1
    else:
        DP[i] = DP[i-L] + DP[i-1]
    DP[i] = DP[i] % mod
print(DP[-1] % mod)
