# -*- coding: utf-8 -*-
"""
本来の予定と使う項目が似通っているから
そこから差分を式で一般化すれば良さそう
前の結果とかから差分で導き出すパターンのやつか

差分は以下になるので、これを本来の予定から引いてやれば良いはず
abs(Ai-1 + Ai) + abs(Ai-Ai+1) - abs(Ai-1-Ai+1)
"""
N = int(input())
A = list(map(int, input().split()))
A.insert(0, 0)
A.append(0)
org = 0
for i in range(1, N + 2):
    org += abs(A[i - 1] - A[i])

for i in range(1, N + 1):
    dif = abs(A[i - 1] - A[i]) + abs(A[i] - A[i + 1]) - abs(A[i - 1] - A[i + 1])
    print(org - dif)
