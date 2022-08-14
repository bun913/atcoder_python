# -*- coding: utf-8 -*-
"""
解く前のメモ

Nが100なので5選ぶのを列挙しても間に合いそう
ただAが非常に大きな数である可能性があるので、計算には工夫が必要と思われる
全てのあまりを出して、掛け合わせて、また最後にあまりを出す必要がある
"""
from itertools import combinations

N, P, Q = list(map(int, input().split()))
A = list(map(int, input().split()))

ans = 0

for a, b, c, d, e in combinations(A, 5):
    if a % P * b % P * c % P * d % P * e % P % P == Q:
        ans += 1
print(ans)
