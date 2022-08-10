# -*- coding: utf-8 -*-
"""
Xから1番左、もしくは一番右にいくまでにかかる最小のコスト
単純にNが100しかないのでどっちのパターンも試せば良いだけ
"""
N, M, X = list(map(int, input().split()))
A = list(map(int, input().split()))
AD = set(A)

# 右にいくパターン
right_cost = 0
for i in range(X, N+1):
    if i in AD:
        right_cost += 1

# 左にいくパターン
left_cost = 0
for i in range(X, -1, -1):
    if i in AD:
        left_cost += 1
ans = min(left_cost, right_cost)
print(ans)
