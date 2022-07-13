# -*- coding: utf-8 -*-
"""
解く前のメモ

Nこの要素を持つ値がわからない整数列A
N-1の要素を持つBが与えられる
Bi >= max(Ai, Ai+1)である
Aの要素の総和として考えられる値の最大値を求める
"""

N = int(input())
B = list(map(int, input().split()))

A = [-1 for _ in range(N)]

for i in range(N):
    # 最初の場合
    if i == 0:
        A[i] = B[i]
        continue
    # Aが最後の場合
    if i == N-1:
        A[i] = B[i-1]
        break
    cur = B[i]
    bef = B[i-1]
    A[i] = min(cur, bef)
print(sum(A))
