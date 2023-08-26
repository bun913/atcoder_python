# -*- coding: utf-8 -*-
"""
解く前のメモ用
"""
N, H, X = map(int, input().split())
P = list(map(int, input().split()))

dif = X - H
for i, p in enumerate(P):
    if p >= dif:
        print(i+1)
        exit()
