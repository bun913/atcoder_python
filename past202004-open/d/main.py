# -*- coding: utf-8 -*-
"""
解く前のメモ用

bit全探索で求められそう
3文字以下の部分文字列を全てつくればいけそうだけど
"""
from sys import setrecursionlimit
from itertools import product

setrecursionlimit(10**7)

S = input()
limit = len(S)

ans_set = set()
for l in range(limit):
    for r in range(l, l + 3):
        part = S[l : r + 1]
        for comb in product([True, False], repeat=len(part)):
            s = ["" for _ in range(len(part))]
            for i, bl in enumerate(comb):
                if bl is True:
                    s[i] = "."
                else:
                    s[i] = part[i]
            ans_set.add("".join(s))
print(len(ans_set))
