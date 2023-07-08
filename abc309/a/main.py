# -*- coding: utf-8 -*-
"""
解く前のメモ用
"""
A, B = map(int, input().split())

if B - A == 1:
    cand = set([1, 2, 4, 5, 7, 8])
    if A in cand:
        print("Yes")
        exit()
print("No")
