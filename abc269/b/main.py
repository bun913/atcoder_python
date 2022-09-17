# -*- coding: utf-8 -*-
"""
"""
S = [list(input()) for _ in range(10)]
A = 11
B = 11
C = 11
D = 11

for i in range(10):
    s = S[i]
    if s.count("#") > 0:
        A = min(A, i + 1)
        B = max(A, i + 1)
        for j in range(10):
            if s[j] == "#":
                C = min(C, j + 1)
                D = max(C, j + 1)
print(A, B)
print(C, D)
