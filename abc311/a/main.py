# -*- coding: utf-8 -*-
"""
解く前のメモ用
"""
N = int(input())
S = input()

a = 0
b = 0
c = 0

for i, s in enumerate(S):
    if s == 'A':
        a += 1
    if s == 'B':
        b += 1
    if s == 'C':
        c += 1
    if a >= 1 and b >= 1 and c >= 1:
        print(i+1)
        exit()
