# -*- coding: utf-8 -*-
"""
解く前のメモ用
"""
N = int(input())
worst_a = -1
worst_score = 10**10


for i in range(N):
    A, B = list(map(int, input().split()))
    worst_a = max(worst_a, A)
    worst_score = min(worst_score, B)
ans = worst_a + worst_score
print(ans)
