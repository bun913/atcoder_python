# -*- coding: utf-8 -*-
"""
i文字目におけるダブルクオートの出現回数をtとする
t%2==0の時に出てくるカンマをドットに置き換えるだけ
"""
from sys import setrecursionlimit

setrecursionlimit(10**7)

N = int(input())
S = list(input())
ans = S[:]
d_cnt = 0

for i, s in enumerate(S):
    if s == '"':
        d_cnt += 1
    if s != ',':
        continue
    if d_cnt % 2 == 0:
        ans[i] = '.'
print(*ans, sep="")
