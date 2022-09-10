# -*- coding: utf-8 -*-
"""
九九を計算して、それぞれの結果を辞書に入れておけば？
一発で求められそう
"""
from collections import defaultdict

N = int(input())

memo = defaultdict(list)

for l in range(1, 10):
    for r in range(1, 10):
        k = l * r
        v = "{} x {}".format(l, r)
        memo[k].append(v)
key = 2025 - N

for v in memo[key]:
    print(v)
