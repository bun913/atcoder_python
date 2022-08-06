# -*- coding: utf-8 -*-
"""
解く前のメモ

Nが100なので数え上げで十分
cをケーキの数として最大25
dをドーナツとして最大14まで数える
"""

N = int(input())

for c in range(26):
    for d in range(15):
        if (c * 4) + (d * 7) == N:
            print('Yes')
            exit()
print('No')
