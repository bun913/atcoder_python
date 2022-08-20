# -*- coding: utf-8 -*-
"""
解く前のメモ

N問がかなり大きいので何も考えず全探索は無理
K分間で得られる最大値を求める
DPでN問目までを使って得られる最適解を求め続ければいけそう?
"""
N, K = list(map(int, input().split()))
DP = [[0 for _ in range(K+1)] for _ in range(N+1)]
A = []
B = []
for i in range(N):
    a, b = list(map(int, input().split()))
    A.append(a)
    B.append(b)

for i in range(1, N+1):
    for j in range(1, K+1):
        full = A[i-1]
        part = B[i-1]
        prev1 = DP[i-1][j-1]
        cand1 = max(prev1 + part, DP[i-1][j])
        cand2 = 0
        if j - 2 >= 0:
            cand2 = DP[i-1][j-2] + full
        DP[i][j] = max(cand1, cand2)
print(DP[-1][-1])
