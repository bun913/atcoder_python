# -*- coding: utf-8 -*-
"""
解く前のメモ用
"""
from statistics import mean
from math import ceil

N = int(input())
A = list(map(int, input().split()))
F = filter(lambda a: a != 0, A)
ans = ceil(mean(F))
print(ans)
