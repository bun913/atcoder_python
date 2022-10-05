# -*- coding: utf-8 -*-
"""
解く前のメモ用

Nの回数もmodを取れば良いのでは？
30回で1回転する
"""
from sys import setrecursionlimit

setrecursionlimit(10**7)

N = int(input())
mod = N % (6 + 1)
cards = [i + 1 for i in range(6)]

for i in range(N % 30):
    l_ind = i % 5
    r_ind = i % 5 + 1
    bef_l = cards[l_ind]
    bef_r = cards[r_ind]
    cards[l_ind] = bef_r
    cards[r_ind] = bef_l
print(*cards, sep="")
