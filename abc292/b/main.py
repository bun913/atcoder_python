# -*- coding: utf-8 -*-
"""
解く前のメモ用
"""
from collections import defaultdict

N, Q = map(int, input().split())
memo = defaultdict(int)

for _ in range(Q):
    c, x = map(int, input().split())
    if c == 1:
        memo[x] += 1
        continue
    if c == 2:
        memo[x] += 2
        continue
    if c == 3:
        if memo[x] >= 2:
            print("Yes")
            continue
        print("No")
