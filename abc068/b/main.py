# -*- coding: utf-8 -*-
"""
Nが100と小さいので単純にやるだけで良い
"""
N = int(input())
cur = 1
while cur <= N:
    cur *= 2
print(cur // 2)
