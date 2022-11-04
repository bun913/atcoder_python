# -*- coding: utf-8 -*-
"""
N個の数。Nは偶数
i=1,2,...NからXiを除いたものの中央値をBiとする
中央値Biを求める
"""
N = int(input())
X = list(map(int, input().split()))
A = sorted(X)
cand1 = A[N // 2 - 1]
cand2 = A[N // 2]

for i in range(N):
    if X[i] <= cand1:
        print(cand2)
    else:
        print(cand1)
