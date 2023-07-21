# -*- coding: utf-8 -*-
"""
解く前のメモ用
よく見ればNが10**9なので全員分の配列を作る段階でTLEになってしまう
なのでdictで管理するのが良さそう
"""
from collections import defaultdict

N, Q = map(int, input().split())
relations = defaultdict(set)

for _ in range(Q):
    t, a, b = map(int, input().split())
    if t == 1:
        relations[a].add(b)
        continue
    if t == 2:
        if b in relations[a]:
            relations[a].remove(b)
        continue
    cand1 = b in relations[a]
    cand2 = a in relations[b]
    if cand1 and cand2:
        print("Yes")
        continue
    print("No")
