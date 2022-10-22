# -*- coding: utf-8 -*-
"""
解く前のメモ用
"""
from collections import defaultdict

N = int(input())
A = list(map(int, input().split()))
memo = defaultdict(int)

for i, a in enumerate(A):
    n = i + 1
    parent = a
    l = 2 * n
    r = 2 * n + 1
    memo[l] = memo[parent] + 1
    memo[r] = memo[parent] + 1

for k in range(2 * N + 1):
    n = k + 1
    print(memo[n])
