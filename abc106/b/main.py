# -*- coding: utf-8 -*-
"""
解く前のメモ

Nが最大で200しかないので全部数え上げでも間に合う
"""
from math import sqrt

N = int(input())
ans = 0

for i in range(1, N+1):
    div_set = set()
    for j in range(1, int(sqrt(i) + 1)):
        if i % j == 0:
            div_set.add(j)
            div_set.add(i // j)
    if len(div_set) == 8 and i % 2 == 1:
        ans += 1
print(ans)
