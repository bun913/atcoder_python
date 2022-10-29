# -*- coding: utf-8 -*-
"""
解く前のメモ用
"""
N = int(input())
H = list(map(int, input().split()))
k = sorted(H, reverse=True)[0]
print(H.index(k) + 1)
