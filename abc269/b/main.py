# -*- coding: utf-8 -*-
"""
"""
S = [list(input()) for _ in range(10)]
A = 11
B = -1
C = 11
D = -1

for i in range(10):
    for j in range(10):
        s = S[i][j]
        if s == "#":
            A = min(A, i + 1)
            B = max(B, i + 1)
            C = min(C, j + 1)
            D = max(D, j + 1)
print(A, B)
print(C, D)
