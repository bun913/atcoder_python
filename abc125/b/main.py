# -*- coding: utf-8 -*-
"""
解く前のメモ

一見DPの問題っぽいが、Nが20なので全探索できる
"""

N = int(input())
V = list(map(int, input().split()))
C = list(map(int, input().split()))

ans = -1

for i in range(2 ** N):
    cost = 0
    value = 0
    for j in range(N):
        if ((i >> j) & 1):
            cost += C[j]
            value += V[j]
    ans = max(ans, value-cost)

print(ans)
