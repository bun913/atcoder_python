# -*- coding: utf-8 -*-
"""
解く前のメモ用
"""
from sys import setrecursionlimit

setrecursionlimit(10**7)
N = int(input())
S = []
A = []

for i in range(N):
    sa = input()
    s, a = sa.split()
    S.append(s)
    A.append(int(a))
# Aのいちばん小さい人のindexを取得
min_index = A.index(min(A))
# min_indexからN人分の名前を出力（あまりをとって円卓を回す)
for i in range(min_index, min_index+N):
    print(S[i % N])
