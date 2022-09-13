# -*- coding: utf-8 -*-
"""
数が5個しかないので愚直に数えるだけで間に合いそう
"""
from itertools import combinations

sums = []
L = list(map(int, input().split()))

for i, j, k in combinations(range(5), 3):
    a = L[i]
    b = L[j]
    c = L[k]
    s = a + b + c
    sums.append(s)

sums_sorted = sorted(sums, reverse=True)
print(sums_sorted[2])
