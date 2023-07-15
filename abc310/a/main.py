# -*- coding: utf-8 -*-
"""
解く前のメモ用
"""
N, P, Q = map(int, input().split())
D = list(map(int, input().split()))
min_ryori = min(D)
cand1 = P
cand2 = Q + min_ryori

print(min(cand1, cand2))
