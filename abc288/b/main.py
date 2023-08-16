# -*- coding: utf-8 -*-
"""
解く前のメモ用
"""
N, K = map(int, input().split())
L = []

for _ in range(N):
    L.append(input())
filterd = L[:K]
filterd.sort()
print(*filterd, sep='\n')
