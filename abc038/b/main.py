# -*- coding: utf-8 -*-
"""
解く前のメモ用
"""
H1, W1 = list(map(int, input().split()))
H2, W2 = list(map(int, input().split()))

if H1 == H2 or H1 == W2 or W1 == H2 or W1 == W2:
    print("YES")
    exit()
print("NO")
