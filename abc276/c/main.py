# -*- coding: utf-8 -*-
"""
解く前のメモ用
辞書順で並べた時PがK番目である
K-1番目の順列を求める

Nが100だからbit全探索は無理
"""
from math import factorial

N = int(input())
P = list(map(int, input().split()))

ind = 0
omomi = N - 1
s = set(P)
# まずPが何番目に大きい順列か求める
for i, p in enumerate(P):
    if i == N - 1:
        ind += 1
    else:
        n = sorted(list(s)).index(p)
        ind += n * factorial(omomi)
        s.remove(p)
        omomi -= 1
ans_ind = ind
