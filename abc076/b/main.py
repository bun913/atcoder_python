# -*- coding: utf-8 -*-
"""
解く前のメモ用
Nが10しかないので全探索できそう
"""
from sys import setrecursionlimit
from itertools import product

setrecursionlimit(10**7)

N = int(input())
K = int(input())

ans = 10**19
for opes in product(["A", "B"], repeat=N):
    cur = 1
    for o in opes:
        if o == "A":
            cur *= 2
            continue
        cur += K
    ans = min(ans, cur)
print(ans)
