# -*- coding: utf-8 -*-
"""
解く前のメモ用
"""
from itertools import combinations

N = int(input())
S = [input() for _ in range(N)]
for comb in combinations(S, 2):
    s1 = comb[0]
    s2 = comb[1]
    cand1 = s1 + s2
    if cand1 == cand1[::-1]:
        print("Yes")
        exit()
    cand2 = s2 + s1
    if cand2 == cand2[::-1]:
        print("Yes")
        exit()
print("No")
