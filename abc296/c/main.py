# -*- coding: utf-8 -*-
"""
解く前のメモ用
"""
from collections import Counter

N, X = map(int, input().split())
A = list(map(int, input().split()))
C = Counter(A)

for a in A:
    rest = a - X
    if C[rest] >= 1:
        print("Yes")
        exit()
print("No")
